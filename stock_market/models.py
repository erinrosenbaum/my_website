from django.db import models

from django.conf import settings
from django.db import models
from django.urls import reverse

class Stock(models.Model):
    symbol = models.CharField(max_length=8)

    def __str__(self):
        return self.symbol

    def get_absolute_url(self):
        return reverse('stock_detail', args=[str(self.id)])
