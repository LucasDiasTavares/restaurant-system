from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import User, UserPJ, Restaurant, Image, Rating, VisitHistory, OpeningHours, CuisineType, Menu, MenuItem


admin.site.register(User)
admin.site.register(UserPJ)
admin.site.register(Restaurant, SimpleHistoryAdmin)
admin.site.register(Image)
admin.site.register(Rating)
admin.site.register(VisitHistory)
admin.site.register(OpeningHours)
admin.site.register(CuisineType)
admin.site.register(Menu)
admin.site.register(MenuItem)
