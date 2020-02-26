from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print ('hanhhanh')
    return render(request, 'pages/home.html')
def contact(request):
    return render(request, 'pages/contact.html')