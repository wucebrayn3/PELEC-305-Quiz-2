from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('registrations/', views.show_registrations, name='show_registrations'),
]