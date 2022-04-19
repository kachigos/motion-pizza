from django.urls import path
from .views import SizePizzaCreateView, SizePizzaListView, SizePizzaUpdateView, SizePizzaDetailView, SizePizzaDeleteView,\
    DoughCreateView, DoughUpdateView, DoughListView, DoughDeleteView, DoughDetailView,\
    DiscountCreateView, DiscountListView, DiscountUpdateView, DiscountDeleteView, DiscountDetailView,\
    DrinksCreateView, DrinksUpdateView, DrinksDeleteView, DrinksDetailView, DrinksListView,\
    FoodCreateView, FoodListView, FoodDeleteView, FoodUpdateView, FoodDetailView,\
    OrderCreateView, OrderlistView, OrderDeleteView, OrderUpdateView, OrderDetailView,\
    PizzaCreateView, PizzaDeleteView, PizzaUpdateView, PizzaListView, PizzaDetailView,\
    StockMainCreateView, StockMainDeleteView, StockMainUpdateView, StockMainListView, StockMainDetailView


urlpatterns = [
    path('sizepizza-create', SizePizzaCreateView.as_view()),
    path('sizepizza-list', SizePizzaListView.as_view()),
    path('sizepizza-update/<int:pk>/', SizePizzaUpdateView.as_view()),
    path('sizepizza-delete/int:pk/', SizePizzaDeleteView.as_view()),
    path('sizepizza-detail/int:pk/', SizePizzaDetailView.as_view()),\

    path('dough-create/', DoughCreateView.as_view()),
    path('dough-list/', DoughListView.as_view()),
    path('dough-detail/<int:pk>/', DoughDetailView.as_view()),
    path('dough-delete/<int:pk>/', DoughDeleteView.as_view()),
    path('dough-update/<int:pk>/', DoughUpdateView.as_view()),

    path('Discount-create/', DiscountCreateView.as_view()),
    path('Discount-list/', DiscountListView.as_view()),
    path('Discount-detail/<int:pk>/', DiscountDetailView.as_view()),
    path('Discount-delete/<int:pk>/', DiscountDeleteView.as_view()),
    path('Discount-update/<int:pk>/', DiscountUpdateView.as_view()),

    path('drinks-create/', DrinksCreateView.as_view()),
    path('drinks-list/', DrinksListView.as_view()),
    path('drinks-detail/<int:pk>/', DrinksDetailView.as_view()),
    path('drinks-delete/<int:pk>/', DrinksDeleteView.as_view()),
    path('drinks-update/<int:pk>/', DrinksUpdateView.as_view()),

    path('food-create/', FoodCreateView.as_view()),
    path('food-list/', FoodListView.as_view()),
    path('food-detail/<int:pk>/', FoodDetailView.as_view()),
    path('food-update/<int:pk>/', FoodUpdateView.as_view()),
    path('food-delete/<int:pk>/', FoodDeleteView.as_view()),

    path('order-create/', OrderCreateView.as_view()),
    path('order-list/', OrderlistView.as_view()),
    path('order-detail/<int:pk/', OrderDetailView.as_view()),
    path('order-delete/<int:pk>/', OrderDeleteView.as_view()),
    path('order-update/<int:pk>/', OrderUpdateView.as_view()),

    path('pizza-create/', PizzaCreateView.as_view()),
    path('pizza-list/', PizzaListView.as_view()),
    path('pizza-detail/<int:pk>/', PizzaDetailView.as_view()),
    path('pizza-delete/<int:pk>/', PizzaDeleteView.as_view()),
    path('pizza-update/<int:pk>/', PizzaUpdateView.as_view()),
    
    path('stockmain-create/', StockMainCreateView.as_view()),
    path('stockmain-list/', StockMainListView.as_view()),
    path('stockmain-detail/<int:pk>/', StockMainDetailView.as_view()),
    path('stockmain-delete/<int:pk>/', StockMainDeleteView.as_view()),
    path('stockmain-update/<int:pk>/', StockMainUpdateView.as_view()),
]