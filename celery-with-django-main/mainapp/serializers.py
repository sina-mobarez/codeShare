from rest_framework import serializers


class InputInfoserializer(serializers.Serializer):
    currency_name = serializers.CharField(max_length=10)
    price = serializers.DecimalField(max_digits=20, decimal_places=2)
    channel_name = serializers.CharField(max_length=200)
    
    
    
    
class InputInfoserializerWb(serializers.Serializer):
    currency_name = serializers.CharField(max_length=10)
    
    