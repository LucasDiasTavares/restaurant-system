from rest_framework import serializers
from .models import User, UserPJ, Restaurant, Image, OpeningHours, CuisineType, Rating, VisitHistory


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserPJSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPJ
        fields = ['id', 'username', 'email']


class CuisineTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CuisineType
        fields = ['name', 'uuid']


class OpeningHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHours
        fields = ['id', 'day_of_week', 'open_time', 'close_time']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']


class RestaurantSerializer(serializers.ModelSerializer):
    cuisine_type = CuisineTypeSerializer()
    opening_hours = OpeningHoursSerializer(many=True)
    # images = ImageSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'city', 'state', 'postal_code', 'phone', 'email', 'description',
                  'cuisine_type', 'opening_hours']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'user', 'restaurant', 'value', 'date']


class VisitHistorySerializer(serializers.ModelSerializer):
    rating = RatingSerializer()

    class Meta:
        model = VisitHistory
        fields = ['id', 'user', 'restaurant', 'rating', 'visit_date', 'next_rating_date']
