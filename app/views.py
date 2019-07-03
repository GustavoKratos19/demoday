from django.shortcuts import render

# Create your views here.

def mostrar_home(request):
    return render(request, 'home.html')
