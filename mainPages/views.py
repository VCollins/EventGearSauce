from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import EquipmentStock


class HomePageView(TemplateView):
    model = EquipmentStock
    template_name = "home.html"


class EquipmentStockListView(ListView):
    model = EquipmentStock
    template_name = "equipment_stock_list.html"


class EquipmentStockDetailView(DetailView):
    model = EquipmentStock
    template_name = "equipment_stock_detail.html"


class EquipmentStockCreateView(CreateView):
    model = EquipmentStock
    template_name = "equipment_stock_new.html"
    fields = [
        "manufacturer",
        "model_name",
        "description",
        "serial_number",
        "amount_available",
    ]


class EquipmentStockUpdateView(UpdateView):
    model = EquipmentStock
    template_name = "equipment_stock_edit.html"
    fields = [
        "manufacturer",
        "model_name",
        "description",
        "serial_number",
        "amount_available",
    ]


class EquipmentStockDeleteView(DeleteView):
    model = EquipmentStock
    template_name = "equipment_stock_delete.html"
    success_url = reverse_lazy("home")


class AboutPageView(TemplateView):
    template_name = "about.html"


class ContactPageView(TemplateView):
    template_name = "contact.html"
