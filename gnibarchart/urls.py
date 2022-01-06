from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='gnibarchart-index'),
    path('barchart/', views.barchart, name='gnibarchart-barchart'),
]
