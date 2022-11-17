from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class EmployeeInfo(APIView):
    def get(self,request):
        emp =Employee.objects.all()
        serializer = EmployeeSerializer(emp, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        serializer = EmployeeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetails(APIView):
    def get(self, request, id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            msg = {'msg': 'Record not found'}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(emp)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            msg = {'msg' : "Record Not Found"}
            return Response(msg, status = status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(emp, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)