from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    path('travel/', views.TravelView.as_view(), name='travel'),
    path('elements/', views.ElementsView.as_view(), name='elements'),

    # countries
    path('travel/thai/', views.ThaiView.as_view(), name='thai'),
    path('travel/srilanka/', views.SriLankaView.as_view(), name='srilanka'),
    path('travel/poland/', views.PolandView.as_view(), name='poland'),
    path('explore-ukraine/', views.ExploreUkraineView.as_view(), name='ukraine'),
]
