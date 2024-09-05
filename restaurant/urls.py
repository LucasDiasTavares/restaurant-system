from django.urls import path
from .views import RestaurantListCreateView, CuisineTypeListView

urlpatterns = [
    path('restaurants/', RestaurantListCreateView.as_view(), name='restaurant-list-create'),
    path('categories/', CuisineTypeListView.as_view(), name='cuisine-type-list'),
]
