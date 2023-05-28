from django.shortcuts import render
from courses.models import Order, Course


def profile(request):
    template = 'account/profile.html'
    user_courses = Order.objects.filter(user=request.user)
    context = {
        'courses': user_courses,
        'user':request.user
    }
    return render(request, template, context)