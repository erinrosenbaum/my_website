from django.conf import settings
from django.db import models
from django.urls import reverse

class City(models.Model):
    name = models.CharField(max_length=30, unique=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('city_detail', args=[str(self.id)])

    class Meta:
        verbose_name_plural = 'cities'
