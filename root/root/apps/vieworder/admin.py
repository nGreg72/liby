from django.contrib import admin

from .models import UserOrderModerateTitle, UserOrderModerateDescription

admin.site.register(UserOrderModerateTitle)
admin.site.register(UserOrderModerateDescription)
