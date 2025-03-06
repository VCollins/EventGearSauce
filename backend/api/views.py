from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, EquipmentStockItemSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import EquipmentStockItem

class EquipmentStockItemListCreate(generics.ListCreateAPIView):
    serializer_class = EquipmentStockItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return EquipmentStockItem.objects.filter(creator=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)
    
class EquipmentStockItemListView(generics.ListAPIView):
    serializer_class = EquipmentStockItemSerializer

    def get_queryset(self):
        return EquipmentStockItem.objects.all()
    
class EquipmentStockItemDeleteView(generics.DestroyAPIView):
    serializer_class = EquipmentStockItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return EquipmentStockItem.objects.filter(creator=user)
    
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]