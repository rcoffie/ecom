from rest_framework import serializers

from product.models import Cart, Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title"]
        read_only_fields = ("id",)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "category",
            "price",
            "stock",
            "status",
            "date_created",
        ]
        read_only_fields = (
            "id",
            "date_created",
        )


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = [
            "id",
            "cart_id",
            "created_at",
            "products",
            "user",
        ]
        read_only_fields = (
            "id",
            "cart_id",
            "user",
        )
