from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from .models import Category,ProductCinema
from .serializers import CategorySerializer,ProductCinemaSerializer
from rest_framework.generics import ListCreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.parsers import MultiPartParser, FormParser


class CategoryListAPI(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer





class ProductCinemaListAPI(ListAPIView):
    queryset = ProductCinema.objects.all()
    serializer_class = ProductCinemaSerializer


class ProductCinemaUpdate(UpdateAPIView):
    queryset = ProductCinema.objects.all()
    serializer_class = ProductCinemaSerializer


class ProductCinemaDelete(DestroyAPIView):
    queryset = ProductCinema.objects.all()
    serializer_class = ProductCinemaSerializer



