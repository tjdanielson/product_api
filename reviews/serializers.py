from rest_framework import serializers
from .models import Review

class ProductSerializer(serializers.ModelSerializer):
    pass
    class Meta:
        model = Review
        fields = ['id', 'username', 'description', 'stars', 'product_id']