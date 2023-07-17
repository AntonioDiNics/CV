from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def fruitstore(request):
    return render(request, "OnlineShoppingPage.html") 

def project2(request):
    return render(request,  "project2.html")

