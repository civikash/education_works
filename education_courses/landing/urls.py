from django. urls import path

from landing.views import landing

app_name = 'landing'

urlpatterns = [
    path('', landing.index, name='index'),
]