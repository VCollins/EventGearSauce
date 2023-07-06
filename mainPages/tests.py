from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse
from .models import EquipmentStock


class EquipmentStockTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.equipmentstock = EquipmentStock.objects.create(
            manufacturer="Shure",
            model_name="SM-58",
            serial_number="1234123412340",
            amount=10,
        )

    def test_model_content(self):
        self.assertEqual(self.equipmentstock.manufacturer, "Shure")
        self.assertEqual(self.equipmentstock.model_name, "SM-58")
        self.assertEqual(self.equipmentstock.serial_number, "1234123412340")
        self.assertEqual(self.equipmentstock.amount, 10)

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
