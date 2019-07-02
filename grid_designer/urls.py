from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('app/', views.index, name='app'),
    path('design/', views.project_grid, name='design'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about')
]