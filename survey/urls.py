from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    path('travel/', views.TravelView.as_view(), name='travel'),
    path('elements/', views.ElementsView.as_view(), name='elements'),
]
