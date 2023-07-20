from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
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


class AboutPageView(TemplateView):
    template_name = "about.html"


class ContactPageView(TemplateView):
    template_name = "contact.html"
