from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, EquipmentStockItemSerializer, QuotationSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import EquipmentStockItem, Quotation

#shows list and allows creation of new equipment stock items (user must authenticated)
class EquipmentStockItemListCreate(generics.ListCreateAPIView):
    serializer_class = EquipmentStockItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return EquipmentStockItem.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

#shows list and allows creation of new quotations (user must authenticated)
class QuotationListCreate(generics.ListCreateAPIView):
    serializer_class = QuotationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):        
        return Quotation.objects.all()
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

#shows list of equipment stock items
class EquipmentStockItemListView(generics.ListAPIView):
    serializer_class = EquipmentStockItemSerializer

    def get_queryset(self):
        return EquipmentStockItem.objects.all()

#shows list of quotations
class QuotationListView(generics.ListAPIView):
    serializer_class = QuotationSerializer

    def get_queryset(self):
        return EquipmentStockItem.objects.all()

#shows list of equipment stock items so that an item may be deleted (user must authenticated)
class EquipmentStockItemDeleteView(generics.DestroyAPIView):
    serializer_class = EquipmentStockItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return EquipmentStockItem.objects.filter(creator=user)

#shows list of quotations so that an item may be deleted (user must authenticated)
class QuotationDeleteView(generics.DestroyAPIView):
    serializer_class = QuotationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Quotation.objects.filter(creator=user)

#allows creation of users    
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]