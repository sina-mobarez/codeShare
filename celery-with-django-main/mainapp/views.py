from django.http import HttpResponse
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .serializers import InputInfoserializer, InputInfoserializerWb
import websocket, json
import pandas as pd 
import dateutil.parser
import datetime
from datetime import date, datetime, timedelta
from .tasks import *
from celery.schedules import crontab
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from django.utils.crypto import get_random_string

# Create your views here.


class WebsocketWay(APIView):
           
    @swagger_auto_schema(request_body=InputInfoserializerWb,
                         responses={400: "something is wrong",
                                    201: "your operation is running"})
    
    def post(self, request,*args, **kwargs): 
        currency_name = request.data['currency_name']
        
        websocket_task(sym=currency_name).delay()
        return HttpResponse("Done")








class HttpWay(APIView):
           
    @swagger_auto_schema(request_body=InputInfoserializer,
                         responses={400: "something is wrong",
                                    201: "your operation is running"})
    
    def post(self, request,*args, **kwargs): 
        currency_name = request.data['currency_name']
        price = request.data['price']
        channel_name = request.data['channel_name']
        
        schedule, created = CrontabSchedule.objects.get_or_create(minute = 1)
        task = PeriodicTask.objects.create(crontab=schedule, name="http_task" + get_random_string(length=4), task='mainapp.tasks.http_task', kwargs={'price': price, 'sym': currency_name, 'channel_name': channel_name})

        return HttpResponse("Done")