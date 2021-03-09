from django.urls import path
from .import views

app_name = 'webapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('feedback/', views.feedback, name='feedback'),
    path('engineering-exams/', views.engineering, name='engineering'),
    path('medical-exams/', views.medical, name='medical'),
    path('defence-exams/', views.defence, name='defence'),
    path('search/', views.search, name='search'),
]
