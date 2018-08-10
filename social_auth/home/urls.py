from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    path('home/', views.home),
    path('prof/', views.prof),
    path('', views.prof),
    path('profile/', views.update_profile),
    path('account/logout/', views.Logout),
]
