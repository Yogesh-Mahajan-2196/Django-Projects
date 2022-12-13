from django.urls import  path
from . import views

urlpatterns = [
    path('ef/', views.employeeview, name='employeeview_url'),
    path('se/', views.showemployee, name='showemployee_url'),
    path('ue/<int:id>/', views.updateemployee, name='updateemployee_url'),
    path('de/<int:id>/', views.deleteemployee, name='deleteemployee_url'),

    path('home/', views.todoview, name= 'home_url'),
    path('showrecords/', views.showrecords, name= 'records_url'),
    path('updaterecords/<int:id>/', views.updaterecords, name= 'updaterecord_url')

]