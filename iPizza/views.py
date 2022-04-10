from rest_framework import generics, permissions
from .models import SizePizza, Dough, Discount, Drinks, Food, Order, Pizza, StockMain
from .serializers import SizePizzaSerializer, DrinksSerializer, DiscountSerializer, DoughSerializer, FoodSerializer, OrderSerializer, PizzaSerializer, StockMainSerializer


class SizePizzaCreateView(generics.CreateAPIView):
    serializer_class = SizePizzaSerializer
    queryset = SizePizza.objects.all()


class SizePizzaListView(generics.ListAPIView):
    serializer_class = SizePizzaSerializer
    queryset = SizePizza.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class SizePizzaUpdateView(generics.UpdateAPIView):
    serializer_class = SizePizzaSerializer
    queryset = SizePizza.objects.all()


class SizePizzaDeleteView(generics.DestroyAPIView):
    serializer_class = SizePizzaSerializer
    queryset = SizePizza.objects.all()


class SizePizzaDetailView(generics.RetrieveAPIView):
    serializer_class = SizePizzaSerializer
    queryset = SizePizza.objects.all()


class DoughCreateView(generics.CreateAPIView):
    serializer_class = DoughSerializer
    queryset = Dough.objects.all()


class DoughListView(generics.ListAPIView):
    serializer_class = DoughSerializer
    queryset = Dough.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class DoughDeleteView(generics.DestroyAPIView):
    serializer_class = DoughSerializer
    queryset = Dough.objects.all()


class DoughUpdateView(generics.UpdateAPIView):
    serializer_class = DoughSerializer
    queryset = Dough.objects.all()


class DoughDetailView(generics.RetrieveAPIView):
    serializer_class = DoughSerializer
    queryset = Dough.objects.all()


class DiscountCreateView(generics.CreateAPIView):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()


class DiscountListView(generics.ListAPIView):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class DiscountUpdateView(generics.UpdateAPIView):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()


class DiscountDeleteView(generics.DestroyAPIView):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()


class DiscountDetailView(generics.RetrieveAPIView):
    serializer_class = DiscountSerializer
    queryset = Discount.objects.all()


class DrinksCreateView(generics.CreateAPIView):
    serializer_class = DrinksSerializer
    queryset = Drinks.objects.all()


class DrinksListView(generics.ListAPIView):
    serializer_class = DrinksSerializer
    queryset = Drinks.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class DrinksDetailView(generics.RetrieveAPIView):
    serializer_class = DrinksSerializer
    queryset = Drinks.objects.all()


class DrinksDeleteView(generics.DestroyAPIView):
    serializer_class = DrinksSerializer
    queryset = Drinks.objects.all()


class DrinksUpdateView(generics.UpdateAPIView):
    serializer_class = DrinksSerializer
    queryset = Drinks.objects.all()


class FoodCreateView(generics.CreateAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()


class FoodListView(generics.ListAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class FoodDetailView(generics.RetrieveAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()


class FoodUpdateView(generics.UpdateAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()


class FoodDeleteView(generics.DestroyAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderlistView(generics.ListAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class OrderDetailView(generics.RetrieveAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderUpdateView(generics.UpdateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class OrderDeleteView(generics.DestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class PizzaCreateView(generics.CreateAPIView):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()


class PizzaListView(generics.ListAPIView):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class PizzaDetailView(generics.RetrieveAPIView):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()


class PizzaUpdateView(generics.UpdateAPIView):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()


class PizzaDeleteView(generics.DestroyAPIView):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()


class StockMainCreateView(generics.CreateAPIView):
    serializer_class = StockMainSerializer
    queryset = StockMain.objects.all()


class StockMainListView(generics.ListAPIView):
    serializer_class = StockMainSerializer
    queryset = StockMain.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class StockMainDetailView(generics.RetrieveAPIView):
    serializer_class = StockMainSerializer
    queryset = StockMain.objects.all()


class StockMainUpdateView(generics.UpdateAPIView):
    serializer_class = StockMainSerializer
    queryset = StockMain.objects.all()


class StockMainDeleteView(generics.DestroyAPIView):
    serializer_class = StockMainSerializer
    queryset = StockMain.objects.all()