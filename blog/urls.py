from django.urls import path
from . import views

urlpatterns = [

    path('', views.post_list, name='post_list'),
    path('', views.sobre_dev, name='sobre_dev'),
]
