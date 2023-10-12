from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, "inicio/home.html")

def gastos(request):
    return render(request, "gasto/gastos.html")
