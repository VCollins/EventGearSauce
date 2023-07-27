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
            description="This is a useful little microphone",
            serial_number="1234123412340",
            amount_available=10,
        )

    def test_model_content(self):
        self.assertEqual(self.equipmentstock.manufacturer, "Shure")
        self.assertEqual(self.equipmentstock.model_name, "SM-58")
        self.assertEqual(self.equipmentstock.serial_number, "1234123412340")
        self.assertEqual(self.equipmentstock.amount_available, 10)
        self.assertEqual(
            self.equipmentstock.description, "This is a useful little microphone"
        )

    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/equipment_stock_detail/1")
        self.assertEqual(response.status_code, 200)

    def test_equipmentstock_listview(self):
        response = self.client.get(reverse("equipment_stock_list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "equipment_stock_list.html")

    def test_equipment_stock_detailview(self):
        response = self.client.get(
            reverse("equipment_stock_detail", kwargs={"pk": self.equipmentstock.pk})
        )
        no_response = self.client.get("/equipment_stock/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Shure")
        self.assertTemplateUsed(response, "equipment_stock_detail.html")

    def test_equipmentstock_createview(self):
        response = self.client.post(
            reverse("equipment_stock_new"),
            {
                "manufacturer": "Denon",
                "model_name": "DJ X1850 Prime",
                "description": "The X1850 Prime is a 4-channel mixing desk with multi-assignable inputs.",
                "serial_number": "0132013201320",
                "amount_available": "2",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(EquipmentStock.objects.last().model_name, "DJ X1850 Prime")

    def test_equipmentStock_updateview(self):
        response = self.client.post(
            reverse("equipment_stock_edit", args="1"),
            {
                "manufacturer": "Denon",
                "model_name": "DJ X1850 Prime",
                "description": "The X1850 Prime has FX Quantization",
                "serial_number": "0132013201320",
                "amount_available": "3",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            EquipmentStock.objects.last().description,
            "The X1850 Prime has FX Quantization",
        )

    def test_equipmentStock_deleteview(self):
        response = self.client.post(reverse("equipment_stock_delete", args="1"))
        self.assertEqual(response.status_code, 302)
