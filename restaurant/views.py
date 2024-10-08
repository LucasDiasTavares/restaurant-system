from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurant, CuisineType
from .serializers import RestaurantSerializer, CuisineTypeSerializer


class CuisineTypeListView(generics.ListAPIView):
    serializer_class = CuisineTypeSerializer
    queryset = CuisineType.objects.all().order_by('name')


class RestaurantListCreateView(generics.ListCreateAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all().order_by('name')

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
