from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
class EmployeeInfo(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    viewsets = Employee.objects.all()
    authentication_classes = [JSONWebTokenAuthentication,]
    permission_classes = [IsAuthenticated,]

