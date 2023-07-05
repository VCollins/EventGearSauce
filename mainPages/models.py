from django.db import models


# Create your models here.
# Equipment datatable
class EquipmentStock(models.Model):
    manufacturer = models.CharField(max_length=50)
    model_name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=13)
    amount = models.IntegerField()

    def __str__(self):
        return str(self.manufacturer) + " " + str(self.model_name)
