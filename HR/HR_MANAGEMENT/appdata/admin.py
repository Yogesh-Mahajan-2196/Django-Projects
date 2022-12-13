from django.contrib import admin
from  .models import Employee, TODO

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'mail', 'addr', 'city', 'mob_no', 'department', 'sal', 'dob']

admin.site.register(Employee,EmployeeAdmin)

class TODOAdmin(admin.ModelAdmin):
    list_display = [ 'work_sheet', 'date']

admin.site.register(TODO,TODOAdmin)