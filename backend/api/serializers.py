from django.contrib.auth.models import User
from rest_framework import serializers
from .models import EquipmentStockItem, Quotation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user

class EquipmentStockItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentStockItem
        fields = ["id", "manufacturer", "model_name", "description", "serial_number", "amount_available", "rental_cost", "creator"]
        extra_kwargs = {"creator": {"read_only": True}}

class QuotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotation
        fields = ["quote_number", "date_created", "client", "equipment", "total_quote_amount", "creator"]
        extra_kwargs = {"creator": {"read_only": True}}