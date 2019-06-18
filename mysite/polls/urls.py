from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, {'spam': 'egg'}, name='index'),
]
