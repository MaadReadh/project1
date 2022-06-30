from django.urls import path
from . import views
# app_name = 'encyclopedia'
urlpatterns = [
   
    path('wiki/create/', views.create_entry, name='create_entry'),
    path('wiki/<str:title>/edit/', views.edit_entry, name='edit_entry'),
    path('wiki/<str:title>/', views.single_entry, name='single_entry'),
    path('wiki/random', views.random_entry, name='random_entry'),
    path("", views.index, name="index"),
    

]