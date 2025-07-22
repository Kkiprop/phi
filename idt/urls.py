# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.collect_data, name='signup'),
    path('confirm/', views.collect_otp, name='collect_otp'),
    path('dashboard/', views.thank_you, name='thank_you'),
    path('', views.home, name='home'),
]
