from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
# Equipment datatable
class EquipmentStockItem(models.Model):
    manufacturer = models.CharField(max_length=50)
    model_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default=None)
    serial_number = models.CharField(max_length=13)
    amount_available = models.IntegerField(default=0)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="equipmentstockitem")

    def __str__(self):
        return str(self.manufacturer) + " " + str(self.model_name)

    def get_absolute_url(self):
        return reverse("equipment_stock_detail", kwargs={"pk": self.pk})