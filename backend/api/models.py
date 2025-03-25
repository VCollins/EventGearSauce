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
    amount_available = models.PositiveIntegerField(default=0)
    rental_cost = models.PositiveIntegerField(default=0)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="equipmentstockitem")

    def __str__(self):
        return str(self.manufacturer) + " " + str(self.model_name)

    def get_absolute_url(self):
        return reverse("equipment_stock_detail", kwargs={"pk": self.pk})

class Quotation(models.Model):
    quote_number = models.PositiveIntegerField(default=1, primary_key=True)
    date_created = models.DateField(auto_now_add=True)
    client = models.CharField(max_length=100)
    equipment = models.ManyToManyField(EquipmentStockItem)
    total_quote_amount = models.PositiveIntegerField(default=0)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quotation")

    def __str__(self):
        return str("Quote number: "+ str(self.quote_number))

    def get_absolute_url(self):
        return reverse("quote_detail", kwargs={"pk": self.quote_number})