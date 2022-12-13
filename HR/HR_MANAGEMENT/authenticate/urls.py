from django.urls import path
from . import views

urlpatterns = [
    path('rv/', views.registerview, name = 'register_url'),
    path('lv/', views.loginview, name = 'loginform_url'),
    path('lgv/', views.logoutview, name = 'logout_url')
]