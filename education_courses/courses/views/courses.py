from django.shortcuts import render
from courses.models import Course


def courses_all(request):
    template = 'courses/courses.html'
    # Получение отправленных данных из запроса
    if request.method == 'POST':
        f_junior = 'f_junior' in request.POST.getlist('special')
        f_middle = 'f_middle' in request.POST.getlist('special')
        f_middle_plus = 'f_middle_plus' in request.POST.getlist('special')
    else:
        f_junior = False
        f_middle = False
        f_middle_plus = False

    courses = Course.objects.all()
    if f_junior:
        courses = courses.filter(special__name='Junior')
    if f_middle:
        courses = courses.filter(special__name='Middle')
    if f_middle_plus:
        courses = courses.filter(special__name='Middle+')
    context = {'courses': courses}
    return render(request, template, context)


def course_detail(request):
    template = 'courses/course_detail.html'
    return render(request, template)