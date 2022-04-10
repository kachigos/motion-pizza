from rest_framework import serializers
from .models import Food, Order, Drinks, SizePizza, Dough, Discount, Pizza, Stock, StockMain


class FoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = Food
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'


class DrinksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drinks
        fields = '__all__'


class SizePizzaSerializer(serializers.ModelSerializer):

    class Meta:
        model = SizePizza
        fields = '__all__'


class DoughSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dough
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Discount
        fields = '__all__'


class PizzaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pizza
        fields = '__all__'


class StockMainSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StockMain
        fields = '__all__'