from django. urls import path

from account.views import login, signup, profile

app_name = 'account'

urlpatterns = [
    path('login/', login.login_view, name='login'),
    path('signup/', signup.signup, name='signup'),
    path('profile/', profile.profile, name='profile')
]