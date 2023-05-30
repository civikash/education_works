from django.shortcuts import render, redirect
from account.models import Account
from django.contrib import messages
import re
from django.core.exceptions import ValidationError


def signup(request):
    template = 'account/signup.html'
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Пароли не совпадают.")
            return redirect('account:signup')

        if Account.objects.filter(email=email).exists():
            messages.error(request, "Пользователь с таким email уже существует.")
            return redirect('account:signup')

        if len(password1) < 6:
            messages.error(request, "Пароль должен содержать не менее 6 символов.")
            return redirect('account:signup')

        if re.search('[а-яА-Я]', password1):
            messages.error(request, "Пароль не может содержать кириллицу.")
            return redirect('account:signup')

        try:
            Account.objects.create_account(email=email, password=password1, first_name=first_name, last_name=last_name)
            messages.success(request, "Вы успешно зарегистрировались.")
            return redirect('account:login')
        except ValidationError as e:
            messages.error(request, e)
            return redirect('account:signup')

    return render(request, template)