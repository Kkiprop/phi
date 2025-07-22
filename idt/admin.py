# admin.py
from django.contrib import admin
from .models import Data, Otpp

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'password', 'confirm_password']
    search_fields = ['username', 'email']


@admin.register(Otpp)
class OtppAdmin(admin.ModelAdmin):
    list_display = ['otp']
