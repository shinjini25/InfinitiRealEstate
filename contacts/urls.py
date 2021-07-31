from django.urls import path
from accounts.urls import urlpatterns
from . import views

urlpatterns=[
    path('contact', views.contact, name= 'contact')
]