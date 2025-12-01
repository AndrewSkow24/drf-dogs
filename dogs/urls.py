from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .apps import DogsConfig
from .views import DogViewSet

app_name = DogsConfig.name

router = DefaultRouter()

router.register("", DogViewSet, "dogs")

urlpatterns = [
    path("breed/", views.BreedListCreateAPIView.as_view(), name="breed_list_create"),
    path(
        "breed/<int:pk>/",
        views.BreedRetrieveUpdateDestroyAPIView.as_view(),
        name="breed_retrieve_update_destroy",
    ),
] + router.urls
