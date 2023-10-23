from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, "travel_app/main.html")

def write(request):
    return render(request, "travel_app/write.html")