from django.urls import path, include
from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.jobs_home, name='jobs_home'),
]
