from django.shortcuts import render

def about(request):
    return render(request, 'sidepages/about.html')

def portfolio(request):
    return render(request, 'sidepages/portfolio.html')

def contact(request):
    return render(request, 'sidepages/contact.html')