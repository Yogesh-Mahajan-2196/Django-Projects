from .views import *
from django.urls import path

urlpatterns = [
    path('ei/', EmployeeInfo.as_view()),
    path('ei/<int:id>/', EmployeeDetails.as_view())
]