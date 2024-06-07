from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name="Наименование датчика")
    description = models.TextField(max_length=150, verbose_name="Описание датчика")


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name="measurements", verbose_name="ID датчика")
    temperature = models.DecimalField(max_digits=4, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
