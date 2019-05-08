import requests
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import DeleteView, CreateView
from django.urls import reverse_lazy
from .forms import StockForm

from . import models
from .models import Stock

def index(request):

    # url for TIME SERIES INTRADAY
    # url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=5min&outputsize=full&apikey=TJ00QDKX97EJGP9K'

    # URL FOR LIQHTWEIGHT QUOTE ENPOINT
    url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey=TJ00QDKX97EJGP9K'
    if request.method == 'POST':
        form = StockForm(request.POST)
        form.save()

    form = StockForm()

    symbols = Stock.objects.all()

    market_data = []

    for symbol in symbols:

        resp = requests.get(url.format(symbol))

        data = resp.json()
        # print(data)
        try:
            my_vol = format(int(data['Global Quote']['06. volume']),",")

            symbol_data = {
                'pk' : symbol.pk,
                'symbol' : symbol.symbol,
                'open': data['Global Quote']['02. open'],
                'high': data['Global Quote']['03. high'],
                'low': data['Global Quote']['04. low'],
                'price': data['Global Quote']['05. price'],
                'volume': my_vol,
            }

        except KeyError:
            symbol_data = {
                'pk' : symbol.pk,
                'symbol' : symbol.symbol,
                'open': "",
                'high': "",
                'low': "",
                'price': "",
                'volume': "",
            }

        market_data.append(symbol_data)
    # print(market_data)
        # else:
        #     symbol.delete()

    context = {'market_data' : market_data, 'form' : form}
    return render(request, 'stock/stock_list.html', context)

class StockDetailView(DetailView):
    model = models.Stock
    template_name = 'stock/stock_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        #print(context)
        # url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=a6be6d4bc61c5dd4dcd359913154cc69'
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&interval=5min&outputsize=full&apikey=TJ00QDKX97EJGP9K'
        my_symbol = Stock.objects.get(pk=self.kwargs['pk'])
        market_data = []
        resp = requests.get(url.format(my_symbol))
        #print("RESPONSE_CONTENT")
        #print(resp.content)
        resp = requests.get(url.format(my_symbol)).json()

        symbol_data = {
            'pk' : self.kwargs['pk'],
            'symbol' : Stock.symbol,
            # #'state' : city.state,
            # 'pressure' : resp['main']['pressure'],
            # 'humidity' : resp['main']['humidity'],
            # 'wind_speed' : resp['wind']['speed'],
            # 'temp_min' : resp['main']['temp_min'],
            # 'temp_max' : resp['main']['temp_max'],
            # 'temperature' : resp['main']['temp'],
            # 'description' : resp['weather'][0]['description'],
            # 'icon' : resp['weather'][0]['icon'],
        }

        market_data.append(symbol_data)
        context['market_data']=market_data

        # print("CONTEXT")
        # print(context)
        # print("WEATHER_DATA")
        # print(weather_data)
        # print("WEATHER_DATA TEMP")
        # print(weather_data[0]['temperature'])

        return context

class StockDeleteView(DeleteView):
    model = models.Stock
    template_name = 'stock/stock_delete.html'
    success_url = reverse_lazy('stock_market:stock_list')

class StockCreateView(CreateView):
    model = models.Stock
    template_name = 'stock/new_stock.html'
    fields = ['symbol']
    success_url = reverse_lazy('stock_market:stock_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
