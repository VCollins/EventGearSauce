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
    path("quotations/",
        views.QuotationListCreate.as_view(),
        name="quotation_list",
    ),
    path("quotations_list/",
        views.QuotationListView.as_view(),
        name="quotation_detail",
    ),
    # TODO: add path for updating quotations
    path("quotations/delete/<int:pk>",
        views.QuotationDeleteView.as_view(),
        name="quotation_delete",
    ),
]
