from django.urls import path
from . import views 

urlpatterns = [
    path("equipment_stock_items/",
        views.EquipmentStockItemListCreate.as_view(),
        name="equipment_stock_list",
    ),
    path("equipment_stock_list/",
        views.EquipmentStockItemListView.as_view(),
        name="equipment_stock_detail",
    ),
    #path(
    #    "equipment_stock/edit/<int:pk>",
    #    views.EquipmentStockItemUpdateView.as_view(),
    #    name="equipment_stock_edit",
    #),
    path("equipment_stock/delete/<int:pk>",
        views.EquipmentStockItemDeleteView.as_view(),
        name="equipment_stock_delete",
    ),
    #path("about", AboutPageView.as_view(), name="about"),
    #path("contact", ContactPageView.as_view(), name="contact"),
]
