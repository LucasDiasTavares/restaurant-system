from django.urls import path
from .views import RestaurantListCreateView, CategoryListView

urlpatterns = [
    path('restaurants/', RestaurantListCreateView.as_view(), name='restaurant-list-create'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
]
