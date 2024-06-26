from django.contrib import admin

from .models import User, UserPJ, Restaurant, Image, Rating, VisitHistory, OpeningHours, Category, Menu, MenuItem


admin.site.register(User)
admin.site.register(UserPJ)
admin.site.register(Restaurant)
admin.site.register(Image)
admin.site.register(Rating)
admin.site.register(VisitHistory)
admin.site.register(OpeningHours)
admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(MenuItem)
