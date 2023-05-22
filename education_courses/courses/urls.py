from django. urls import path

from courses.views import courses

app_name = 'courses'

urlpatterns = [
    path('all/', courses.courses_all, name='courses-all'),
]