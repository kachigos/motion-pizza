from django.urls import path
from .views import DeliveryCreateView, DeliveryListView, DeliveryUpdateView , DeliveryDetailView, DeliveryDeleteView


urlpatterns = [
    path('delivery-create', DeliveryCreateView.as_view()),
    path('delivery-list', DeliveryListView.as_view()),
    path('delivery-update/<int:pk>/', DeliveryUpdateView.as_view()),
    path('delivery-delete/int:pk/', DeliveryDeleteView.as_view()),
    path('delivery-detail/int:pk/', DeliveryDetailView.as_view()),
]