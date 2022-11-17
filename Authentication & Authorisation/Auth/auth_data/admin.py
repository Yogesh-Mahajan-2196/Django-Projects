from django.contrib import admin

# Register your models here.
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll_no', 'name', 'marks', 'add']

admin.site.register(Student,StudentAdmin)