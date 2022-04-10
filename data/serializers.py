from rest_framework import serializers
from .models import Topic, City, Data, About


class TopicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Topic
        fields = '__all__'
        
        
class CitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = City
        fields = '__all__'
    

class DataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Data
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = About
        fields = '__all__'       