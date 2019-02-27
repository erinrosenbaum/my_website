from django.shortcuts import render

from .models import Job

def jobs_home(request):
    jobs = Job.objects
    return render(request, 'jobs/jobs_home.html', {'jobs': jobs})
