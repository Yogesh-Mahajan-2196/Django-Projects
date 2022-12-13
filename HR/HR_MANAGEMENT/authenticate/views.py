from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import MyuserCreationForm


def registerview(request):
    form = MyuserCreationForm()
    template_name = 'authenticate/register.html'

    if request.method == "POST":
        form = MyuserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loginform_url')
    context = {'form': form}
    return render(request, template_name, context)


def loginview(request):
    template_name = 'authenticate/loginform.html'
    context = {}
    if request.method == "POST":
        un = request.POST.get('un')
        pw = request.POST.get('pw')

        user = authenticate(username=un, password=pw)
        if user is not None:
            login(request,user)
            return redirect('home_url')
    return render(request, template_name, context)


def logoutview(request):
    logout(request)
    return redirect('loginform_url')
