from rest_framework import serializers
from .models import Delivery, Address, Payment


class DeliverySerializer(serializers.ModelSerializer):
    
    class Meta:   
        model = Delivery
        fields = '__all__'
        
        
class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = '__all__'
        
        
class PaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields = '__all__'