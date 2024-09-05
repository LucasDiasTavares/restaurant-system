from uuid import uuid4
from django.db import models
from datetime import timedelta
from simple_history.models import HistoricalRecords


# fake user
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"Client: {self.username}"


class UserPJ(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"Restaurant Owner: {self.username}"


class CuisineType(models.Model):
    name = models.CharField(max_length=100)
    history = HistoricalRecords()
    uuid = models.UUIDField(default=uuid4, editable=False, db_index=True)

    def __str__(self):
        return self.name


class OpeningHours(models.Model):
    day_of_week = models.CharField(max_length=9, choices=[
        ('Segunda', 'Segunda'),
        ('Terça', 'Terça'),
        ('Quarta', 'Quarta'),
        ('Quinta', 'Quinta'),
        ('Sexta', 'Sexta'),
        ('Sabado', 'Sabado'),
        ('Domingo', 'Domingo')
    ])
    open_time = models.TimeField()
    close_time = models.TimeField()

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.day_of_week} {self.open_time} - {self.close_time}"


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.name} - {self.price}"


class Menu(models.Model):
    name = models.CharField(max_length=255)
    item = models.ManyToManyField(MenuItem, related_name='menu')

    history = HistoricalRecords()

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    description = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(UserPJ, related_name='userpj', on_delete=models.CASCADE, default=None)
    cuisine_type = models.ForeignKey(CuisineType, related_name='type', on_delete=models.CASCADE, default=None)
    opening_hours = models.ManyToManyField(OpeningHours, related_name='restaurant')
    menu = models.ManyToManyField(Menu, related_name='menu_restaurant', default=None)

    history = HistoricalRecords()

    def __str__(self):
        average_rating = self.calculate_average_rating()
        return f"{self.name} - Average Rating: {average_rating:.2f}"

    def calculate_average_rating(self):
        ratings = self.rating_set.all()
        if ratings.exists():
            total_ratings = sum(rating.value for rating in ratings)
            average = total_ratings / ratings.count()
            return average
        return 0


class Image(models.Model):
    # AWS integration
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.image


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    value = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} -> {self.restaurant}: {self.value}"


class VisitHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    visit_date = models.DateTimeField(auto_now_add=True)
    next_rating_date = models.DateTimeField()
    approved_by = models.ForeignKey(UserPJ, related_name='approved_by', on_delete=models.CASCADE, default=None)
    approved = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return f"{self.user} visited {self.restaurant} on {self.visit_date}"

    def save(self, *args, **kwargs):
        # Set the next rating date to 7 days after the visit date
        if not self.next_rating_date:
            self.next_rating_date = self.visit_date + timedelta(days=7)
        super().save(*args, **kwargs)
