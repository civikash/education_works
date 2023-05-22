from django.shortcuts import render


def index(request):
    template = 'landing/app.html'
    return render(request, template)