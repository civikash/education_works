from django. urls import path

from courses.views import courses

app_name = 'courses'

urlpatterns = [
    path('all/', courses.courses_all, name='courses-all'),
    path('course/<uuid:uid>/', courses.course_detail, name='courses-detail'),
    path('course/order/', courses.course_order, name='courses-order'),
]