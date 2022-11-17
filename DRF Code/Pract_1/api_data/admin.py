from django.contrib import admin

from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eid', 'ename', 'eadd', 'esal']

admin.site.register(Employee,EmployeeAdmin)