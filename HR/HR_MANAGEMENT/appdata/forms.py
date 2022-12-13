from  django import forms
from .models import Employee,TODO

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

        labels ={
            'name': 'NAME',
            'mail': 'EMAIL_ID',
            'addr': 'ADDRESS',
            'city': 'CITY',
            'mob_no': 'MOBILE_NUMBER',
            'department': 'DEPARTMENT',
            'sal': 'SALARY',
            'dob': 'DATE_OF_BIRTH',
        }

        widgets ={
            'name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'mail': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'addr': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'mob_no': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'department': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'sal': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'dob': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            })
        }

class TODOForm(forms.ModelForm):
    class Meta:
        model = TODO
        fields = '__all__'

        labels = {
        'work_sheet': 'WORK_SHEET',
        'date': 'DATE'
        }

        widgets = {
        'date': forms.DateInput(attrs={
            'type': 'date'
        })
        }