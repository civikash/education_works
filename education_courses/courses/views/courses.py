from django.shortcuts import render, redirect
from courses.models import Course, Order, Directions, TypeEducation, Temp, Option, Package, Target
import uuid
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.http import JsonResponse


def courses_search(request, course_name=None, select_course=None ):
    template = 'courses/courses.html'

    if request.method == 'POST':
            selected_specials = request.POST.getlist('special')
            selected_directions = request.POST.getlist('directions')
            selected_devices = request.POST.getlist('devices')
            search_query = request.POST.get('search')
    else:
        selected_specials = []
        selected_devices = []
        selected_directions = []
        search_query = None

    courses = Course.objects.all()
    print("select_course", select_course)
    if selected_devices:
        courses = courses.filter(device__name__in=selected_devices)
    if selected_directions:
        courses = courses.filter(directions__name__in=selected_directions)
    if selected_specials:
        courses = courses.filter(special__name__in=selected_specials)
    if search_query:
        courses = courses.filter(title__icontains=search_query)
    if course_name:
        courses = Course.objects.filter(title=course_name)
    if select_course is not None or course_name == None:
        courses = Course.objects.filter(directions=select_course)
    else:
        courses = Course.objects.all()
         
    context = {'courses': courses, 'course_name':course_name, 'select_course':select_course}
    return render(request, template, context)


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
        selected_devices = []
        selected_directions = []
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
    context = {'courses': courses }
    return render(request, template, context)


def course_detail(request, uid):
    course = get_object_or_404(Course, uid=uid)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        value_main = request.POST.get('value_main')

        order = Order(
                user = request.user,
                directions=course.directions,
                name=name,
                email=email,
                phone_number=phone_number,
                value=value_main
            )
        order.save()
        return redirect('account:profile')
    
    template = 'courses/course_detail.html'
    context = {'course': course}
    return render(request, template, context)


def course_order(request):
    if request.method == 'POST':
        directions_ids = request.POST.getlist('directions')
        typeEducation = request.POST.getlist('typeEducation')
        package_ids = request.POST.getlist('package')
        temp_id = request.POST.getlist('temp')
        name = request.POST.get('name')
        email = request.POST.get('email')
        option_ids = request.POST.getlist('option')
        phone_number = request.POST.get('phone_number')
        targets_ids = request.POST.getlist('target')
        value = request.POST.get('value_all_total')

        directions = Directions.objects.filter(id__in=directions_ids)
        education = TypeEducation.objects.filter(id__in=typeEducation)
        targets_f = Target.objects.filter(id__in=targets_ids)
        package = Package.objects.filter(id__in=package_ids)
        temp = Temp.objects.filter(id__in=temp_id)
        option = Option.objects.filter(id__in=option_ids)



        order = Order(
            user=request.user,
            directions=directions.first(),
            package=package.first(),
            temp=temp.first(),
            name=name,
            email=email,
            type_education=education.first(),
            phone_number=phone_number,
            value=value
            )
        order.save()
        order.target.set(targets_f)
        order.option.set(option)
        return redirect('account:profile')

    directions = Directions.objects.all()
    options = Option.objects.all()
    temps = Temp.objects.all()
    targets = Target.objects.all()
    typeEducation = TypeEducation.objects.all()
    package = Package.objects.all()

    template = 'courses/course_order.html'
    context = {'directions':directions, 'typeEducation':typeEducation, 'options': options, 'temps': temps, 'packages': package, 'targets': targets}
    return render(request, template, context)


def course_delete(request, uid):
    print(uid)
    try:
        course = Order.objects.get(uid=uid)
        course.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Order.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Course not found'})
    except Exception as e:
        return JsonResponse({'success': False, 'message': str(e)})