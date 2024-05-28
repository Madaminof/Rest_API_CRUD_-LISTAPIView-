from .models import Category,ProductCinema
from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)




    class Meta:
        model = Category
        fields = '__all__'


class ProductCinemaSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    video = serializers.FileField()
    audio = serializers.FileField()
    image = serializers.ImageField()

    class Meta:
        model = ProductCinema
        fields = '__all__'

