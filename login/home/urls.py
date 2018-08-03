from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    path('', views.Home),
    path('profile/', views.update_profile),
    path('account/logout/', views.Logout),
]
