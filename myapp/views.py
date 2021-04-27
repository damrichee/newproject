from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome Damilola")

#User Register
def Register(request):
    render(request, 'registration/register.html')
