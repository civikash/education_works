from django.shortcuts import render
from courses.models import Course
import uuid
from django.shortcuts import get_object_or_404


def courses_all(request):
    template = 'courses/courses.html'
    # Получение отправленных данных из запроса
    if request.method == 'POST':
            selected_specials = request.POST.getlist('special')
            selected_directions = request.POST.getlist('directions')
            selected_devices = request.POST.getlist('devices')
            search_query = request.POST.get('search')
    else:
        selected_specials = []
        search_query = None

    courses = Course.objects.all()
    if selected_devices:
         courses = courses.filter(device__name__in=selected_devices)
    if selected_directions:
         courses = courses.filter(directions__name__in=selected_directions)
    if selected_specials:
            courses = courses.filter(special__name__in=selected_specials)
    if search_query:
        courses = courses.filter(title__icontains=search_query)
    context = {'courses': courses}
    return render(request, template, context)


def course_detail(request, uid):
    course = get_object_or_404(Course, uid=uid)
    template = 'courses/course_detail.html'
    context = {'course': course}
    return render(request, template, context)