
from celery import shared_task
import websocket, json
import pandas as pd 
import dateutil.parser
import datetime
from datetime import datetime, timedelta
import redis
import requests
import pandas as pd




minutes_processed = {}
minute_candlesticks = []
current_tick = None
previous_tick = None

socket = 'wss://ws-feed.pro.coinbase.com'

def on_open(ws, sym):
	print("Connection is opened")
	subscribe_msg = {
		"type": "subscribe",
		"channels": [
			{
			"name": "ticker",
			"product_ids": [
				sym
				]
			}

		]
	}

	ws.send(json.dumps(subscribe_msg))

def on_message(ws, message):
	global current_tick, previous_tick

	previous_tick = current_tick
	current_tick = json.loads(message)


	print(f"{current_tick['price']} @ {current_tick['time']}")

	tick_datetime_object = dateutil.parser.parse(current_tick['time'])
	timenow = tick_datetime_object + timedelta(hours=8)
	tick_dt = timenow.strftime("%m/%d/%Y %H:%M")
	print(tick_datetime_object.minute)
	print(tick_dt)

	if not tick_dt in minutes_processed:
		print("This is a new candlestick")
		minutes_processed[tick_dt] = True

		if len(minute_candlesticks) > 0:
			minute_candlesticks[-1]['close'] = previous_tick['price']

		minute_candlesticks.append({
			'minute': tick_dt,
			'open': current_tick['price'],
			'high': current_tick['price'],
			'low': current_tick['price']
			})

		df = pd.DataFrame(minute_candlesticks[:-1])

	if len(minute_candlesticks) > 0:
		current_candlestick = minute_candlesticks[-1]
		if current_tick['price'] > current_candlestick['high']:
			current_candlestick['high'] = current_tick['price']
		if current_tick['price'] < current_candlestick['low']:
			current_candlestick['low'] = current_tick['price']

		print("== Candlesticks ==")
		for candlestick in minute_candlesticks:
			print(candlestick)




@shared_task(bind=True)
def websocket_task(self, sym):
    ws = websocket.WebSocketApp(socket, on_open=on_open(sym), on_message=on_message)
    ws.run_forever()
    return "Done"


#-------------------api-----------------------------


r = redis.Redis(host='localhost', port=6379, db=0)


@shared_task(bind=True)
def http_task(self, **kwargs):
    
    api_url = "https://api.pro.coinbase.com"

    sym = kwargs['sym']
    
    price = kwargs['price']

    bar_size = "60"

    time_end = datetime.now()

    delta = timedelta(minutes=1)

    time_start = time_end - (300*delta)

    time_start = time_start.isoformat()
    time_end = time_end.isoformat()




    parameters = {
        "start": time_start,
        "end": time_end,
        "granularity": bar_size
    }


    data = requests.get(f'{api_url}/products{sym}/candles',
                        params= parameters,
                        headers= {'content-type': 'application/json'})


    df = pd.DataFrame(data.json(),
                    columns= ['time', 'low', 'high', 'open', 'close', 'volume'])

    df['date'] = pd.to_datetime(df['time'], unit='s')
    df = df[['date', 'open', 'high', 'low', 'close']]

    df.set_index('date', inplace= True)

    df = df.resample('1 min').agg({
        'open': 'first',
        'high': 'max',
        'low': 'min',
        'close': 'last'})

    
    
    return r.publish(kwargs['channel_name'], df)
