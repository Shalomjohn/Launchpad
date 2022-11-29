from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def own(request):
    return render(request, 'main/own.html')