from django.shortcuts import render


def courses_all(request):
    template = 'courses/courses.html'
    return render(request, template)


def course_detail(request):
    template = 'courses/course_detail.html'
    return render(request, template)