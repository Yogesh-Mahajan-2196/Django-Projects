from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

# class StudentInfo(viewsets.ModelViewSet):
#     serializer_class = StudentSerializer
#     queryset = Student.objects.all()

class StudentDetails(viewsets.ViewSet):
    
    def list(self,request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self,request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request,pk):
        try:
            std = Student.objects.get(id = pk)
        except Student.DoesNotExist:
            return Response({'msg': 'Student Does Not Exist'})
        serializer = StudentSerializer(std, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrive(self,request,pk):
        try:
            stu = Student.objects.get(id = pk)
        except Student.DoesNotExist:
            return Response({'msg': 'Student Does Not Exist'})
        serializer = StudentSerializer(stu)
        return Response(serializer.sata, status = status.HTTP_200_OK)

    def destroy(self, request, pk):
        try:
            std = Student.objects.get(id = pk)
        except Student.DoesNotExist:
            msg = {'msg':'record not found'}
            return Response(msg , status=status.HTTP_404_NOT_FOUND)
        std.delete()
        return Response({'msg': 'DELETE SUCCESSFULLY'} , status=status.HTTP_205_RESET_CONTENT)
