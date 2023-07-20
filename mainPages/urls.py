from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    ContactPageView,
    EquipmentStockListView,
    EquipmentStockDetailView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path(
        "equipment_stock", EquipmentStockListView.as_view(), name="equipment_stock_list"
    ),
    path(
        "equipment_stock/<int:pk>",
        EquipmentStockDetailView.as_view(),
        name="equipment_stock_detail",
    ),
    path("about", AboutPageView.as_view(), name="about"),
    path("contact", ContactPageView.as_view(), name="contact"),
]
