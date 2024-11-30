from django.shortcuts import render

from django.shortcuts import render

def home_view(request):

    return render(request, 'main/home.html')

def about_view(request):

    return render(request, 'main/about.html')
