from django.shortcuts import render, redirect
from courses.models import Directions


def index(request):
    template = 'landing/app.html'

    directions = Directions.objects.all()
    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        select_course = request.POST.get('select_course')
        if course_name and select_course:
            # Оба значения переданы, перенаправляем на другой метод с двумя параметрами
            return redirect('courses:courses-search', course_name=course_name, select_course=select_course)
        elif course_name:
            # Передано только значение course_name
            return redirect('courses:courses-search', course_name=course_name, select_course=None)
        elif select_course:
            # Передано только значение select_course
            return redirect('courses:courses-search', course_name=None, select_course=select_course)
        else:
            # Не передано ни одно значение
            return redirect('courses:courses-search', course_name=None, select_course=None)
    context = {
    'request': request,
    'directions': directions
    }
    return render(request, template, context)