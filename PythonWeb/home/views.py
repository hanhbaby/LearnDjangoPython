from django.shortcuts import render
from . forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    #user = User.objects.first()
    #print(user)
    return render(request, 'pages/home.html')
   # return render(request, 'pages/home.html', {'user' : user})
def contact(request):
    return render(request, 'pages/contact.html')
def error(request):
    return render(request, 'pages/error.html')
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})