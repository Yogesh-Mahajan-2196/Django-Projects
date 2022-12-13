from django.shortcuts import render,redirect
from .models import Employee,TODO
from .forms import EmployeeForm,TODOForm
from django.contrib.auth.decorators import login_required

@login_required(login_url = 'loginform_url')
def employeeview(request):
    form = EmployeeForm()
    template_name = 'appdata/employeeform.html'
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showemployee_url')
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url = 'loginform_url')
def showemployee(request):
    data = Employee.objects.all()
    template_name = 'appdata/showemployee.html'
    context = {'data': data}
    return render(request, template_name, context)

def updateemployee(request,id):
    obj = Employee.objects.get(id = id)
    form = EmployeeForm(instance=obj)
    template_name = 'appdata/employeeform.html'
    context = {'form': form}

    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('showemployee_url')
    return render(request, template_name, context)

def deleteemployee(request,id):
    obj = Employee.objects.get(id=id)
    template_name = 'appdata/confirmation.html'
    context = {'obj': obj}
    if request.method == 'POST':
        obj.delete()
        return redirect('showemployee_url')
    return render(request, template_name, context)

@login_required(login_url = 'loginform_url')
def todoview(request):
    form = TODOForm()
    template_name = 'appdata/home.html'
    if request.method == 'POST':
        form = TODOForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('records_url')
    context = {'form': form}
    return render(request, template_name, context)

@login_required(login_url = 'loginform_url')
def showrecords(request):
    data = TODO.objects.all()
    template_name = 'appdata/workdata.html'
    context = {'data': data}
    return render(request, template_name, context)

def updaterecords(request,id):
    obj = TODO.objects.get(sr_no = id)
    form = TODOForm(instance=obj)
    template_name = 'appdata/home.html'
    context = {'form': form}

    if request.method == "POST":
        form = TODOForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('records_url')
    return render(request, template_name, context)
