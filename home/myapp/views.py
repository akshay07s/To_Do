from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#return HttpResponse("<b>Hello welcome<b>")
def home(request):
    return render(request , "myapp/index.html")
def about(request):
    return render(request , "myapp/about.html")
def contact(request):
    return render(request , "myapp/contact.html")
def services(request):
    return render(request , "myapp/services.html")