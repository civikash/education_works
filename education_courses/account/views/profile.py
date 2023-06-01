from django.shortcuts import render, redirect
from courses.models import Order, Course
from account.models import Account
from pytz import all_timezones
from django.contrib.auth import logout
from datetime import datetime
from django.views.generic import View
from django.contrib import messages


def profile(request):
    template = 'account/profile.html'
    user_courses = Order.objects.filter(user=request.user)
    context = {
        'courses': user_courses,
        'user':request.user
    }
    return render(request, template, context)


def update_profile(request):
    template = 'account/edit_profile.html'
    user_courses = Order.objects.filter(user=request.user)

    if request.method == 'POST':
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        patron = request.POST.get('patron')
        gender = request.POST.get('gender')
        birthdata = request.POST.get('birthdate')
        timezone = request.POST.get('timezone')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        country = request.POST.get('country')
        city = request.POST.get('city')
        bio = request.POST.get('bio')
        interests = request.POST.get('interests')

        try:
            datetime.strptime(birthdata, '%Y-%m-%d')
        except ValueError:
            messages.error(request, 'Некорректный формат даты рождения. Используйте формат YYYY-MM-DD')
            return redirect('account:profile')
        
        if len(phone_number) != 11:
            messages.error(request, 'Некорректная длина номера телефона. Должно быть 11 символов')
            return redirect('account:profile')

        user = request.user
        user.email = email
        user.patronymic = patron
        user.birthday = birthdata or None
        user.time = timezone
        user.myself = bio or None
        user.hobby = interests or None
        user.number = phone_number or None
        user.country = country
        user.city = city
        user.gender = str(gender)
        user.last_name = last_name
        user.first_name = name
        user.save()
        return redirect('account:profile')

    context = {
        'courses': user_courses,
        'user':request.user,
        'time_zones': all_timezones,
        'gender_choices': Account.GENDER
    }
    return render(request, template, context)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('account:login')
