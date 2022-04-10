from rest_framework import generics, permissions

from .serializers import TopicSerializer, CitySerializer, DataSerializer, AboutSerializer
from .models import Topic, City, Data, About


class TopicCreateView(generics.CreateAPIView):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()


class TopicListView(generics.ListAPIView):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class TopicUpdateView(generics.UpdateAPIView):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()


class TopicDeleteView(generics.DestroyAPIView):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()


class TopicDetailView(generics.RetrieveAPIView):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
    
    
class CityCreateView(generics.CreateAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()
    
    
class CityListView(generics.ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class CityUpdateView(generics.UpdateAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()
    

class CityDeleteView(generics.DestroyAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class CityDetailView(generics.RetrieveAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()
    
    
class DataCreateView(generics.CreateAPIView):
    serializer_class = DataSerializer
    queryset = Data.objects.all()
    
    
class DataListView(generics.ListAPIView):
    serializer_class = DataSerializer
    queryset = Data.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class DataUpdateView(generics.UpdateAPIView):
    serializer_class = DataSerializer
    queryset = Data.objects.all()
    

class DataDeleteView(generics.DestroyAPIView):
    serializer_class = DataSerializer
    queryset = Data.objects.all()


class DataDetailView(generics.RetrieveAPIView):
    serializer_class = DataSerializer
    queryset = Data.objects.all()   

    
class AboutCreateView(generics.CreateAPIView):
    serializer_class = AboutSerializer
    queryset = About.objects.all()
    
    
class AboutListView(generics.ListAPIView):
    serializer_class = AboutSerializer
    queryset = About.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    
class AboutUpdateView(generics.UpdateAPIView):
    serializer_class = AboutSerializer
    queryset = About.objects.all()
    

class AboutDeleteView(generics.DestroyAPIView):
    serializer_class = AboutSerializer
    queryset = About.objects.all()


class AboutDetailView(generics.RetrieveAPIView):
    serializer_class = AboutSerializer
    queryset = About.objects.all()