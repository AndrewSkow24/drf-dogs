from rest_framework.viewsets import ModelViewSet
from .serializers import DogSerializer, BreedSerializer
from .models import Dog, Breed
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# Dog - ViewSet
class DogViewSet(ModelViewSet):
    serializer_class = DogSerializer
    queryset = Dog.objects.all()


# Breed - Generics
class BreedListCreateAPIView(ListCreateAPIView):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()


class BreedRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BreedSerializer
    queryset = Breed.objects.all()
