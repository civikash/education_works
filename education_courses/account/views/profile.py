from django.shortcuts import render


def profile(request):
    template = 'account/profile.html'
    context = {
        'user':request.user
    }
    return render(request, template, context)