from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.index, name='main'),  # главная страница
    path('news/', views.news, name='news'),
    path('management/', views.management, name='management'),
    path('facts/', views.facts, name='facts'),
    path('contacts/', views.contacts, name='contacts'),
]