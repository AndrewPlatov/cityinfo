from django.shortcuts import render

def index(request):
    return render(request, 'mainpage/main.html')

def news(request):
    return render(request, 'mainpage/news.html')

def management(request):
    return render(request, 'mainpage/management.html')

def facts(request):
    return render(request, 'mainpage/facts.html')

def contacts(request):
    return render(request, 'mainpage/contacts.html')