import requests
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import City
from .forms import CityForm
from . import models

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=a6be6d4bc61c5dd4dcd359913154cc69'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        resp = requests.get(url.format(city))
        #print(resp.content)
        resp = requests.get(url.format(city)).json()

        city_weather = {
            'pk' : city.pk,
            'name' : city.name,
            #'state' : city.state,
            'temp_min' : resp['main']['temp_min'],
            'temp_max' : resp['main']['temp_max'],
            'temperature' : resp['main']['temp'],
            'description' : resp['weather'][0]['description'],
            'icon' : resp['weather'][0]['icon'],
        }

        weather_data.append(city_weather)

    context = {'weather_data' : weather_data, 'form' : form}
    return render(request, 'weather.html', context)

class CityDetailView(DetailView):
    model = models.City
    template_name = 'city_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        #print(context)
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=a6be6d4bc61c5dd4dcd359913154cc69'
        my_city = City.objects.get(pk=self.kwargs['pk'])
        weather_data = []
        resp = requests.get(url.format(my_city))
        #print("RESPONSE_CONTENT")
        #print(resp.content)
        resp = requests.get(url.format(my_city)).json()

        city_weather = {
            'pk' : self.kwargs['pk'],
            'name' : City.name,
            #'state' : city.state,
            'temp_min' : resp['main']['temp_min'],
            'temp_max' : resp['main']['temp_max'],
            'temperature' : resp['main']['temp'],
            'description' : resp['weather'][0]['description'],
            'icon' : resp['weather'][0]['icon'],
            'time' : datetime.datetime.now()
        }

        weather_data.append(city_weather)
        context['weather_data']=weather_data

        # print("CONTEXT")
        # print(context)
        # print("WEATHER_DATA")
        # print(weather_data)
        # print("WEATHER_DATA TEMP")
        # print(weather_data[0]['temperature'])

        return context

class CityDeleteView(DeleteView):
    model = models.City
    template_name = 'city_delete.html'
    success_url = reverse_lazy('weather:weather_list')

class CityCreateView(CreateView):
    model = models.City
    template_name = 'new_city.html'
    fields = ['name']
    success_url = reverse_lazy('weather:weather_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
