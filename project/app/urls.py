from django.urls import path
from app import views

urlpatterns=[
    path('', views.my_fillter, name='my_fillter')
]