from django.urls import path
from .views import TopicCreateView, TopicListView, TopicUpdateView, TopicDetailView, TopicDeleteView,\
    CityCreateView, CityUpdateView, CityListView, CityDeleteView, CityDetailView,\
    DataCreateView, DataListView, DataUpdateView, DataDeleteView, DataDetailView,\
    AboutCreateView, AboutUpdateView, AboutDeleteView, AboutDetailView, AboutListView


urlpatterns = [
    path('topic-create', TopicCreateView.as_view()),
    path('topic-list', TopicListView.as_view()),
    path('topic-update/<int:pk>/', TopicUpdateView.as_view()),
    path('topic-delete/int:pk/', TopicDeleteView.as_view()),
    path('topic-detail/int:pk/', TopicDetailView.as_view()),\

    path('city-create/', CityCreateView.as_view()),
    path('city-list/', CityListView.as_view()),
    path('city-detail/<int:pk>/', CityDetailView.as_view()),
    path('city-delete/<int:pk>/', CityDeleteView.as_view()),
    path('city-update/<int:pk>/', CityUpdateView.as_view()),

    path('data-create/', DataCreateView.as_view()),
    path('data-list/', DataListView.as_view()),
    path('data-detail/<int:pk>/', DataDetailView.as_view()),
    path('data-delete/<int:pk>/', DataDeleteView.as_view()),
    path('data-update/<int:pk>/', DataUpdateView.as_view()),

    path('about-create/', AboutCreateView.as_view()),
    path('about-list/', AboutListView.as_view()),
    path('about-detail/<int:pk>/', AboutDetailView.as_view()),
    path('about-delete/<int:pk>/', AboutDeleteView.as_view()),
    path('about-update/<int:pk>/', AboutUpdateView.as_view()),
]