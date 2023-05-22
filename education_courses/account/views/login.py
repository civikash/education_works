from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

def login_view(request):
    template = 'account/login.html'
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Вы успешно вошли в систему.")
            return redirect('account:profile')  # Перенаправление на главную страницу после успешного входа
        else:
            messages.error(request, "Неправильный email или пароль.")
            return redirect('account:login')  # Перенаправление на страницу входа в случае ошибки
    return render(request, template)