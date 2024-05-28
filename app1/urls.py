from .views import CategoryListAPI,ProductCinemaListAPI,ProductCinemaUpdate,ProductCinemaDelete
from django.urls import path

urlpatterns = [
    path('category/', CategoryListAPI.as_view()),
    path('product/', ProductCinemaListAPI.as_view()),
    path('product/<int:pk>/', ProductCinemaUpdate.as_view()),
    path('product_delete/<int:pk>/', ProductCinemaDelete.as_view()),
    path('product_update/<int:pk>/', ProductCinemaUpdate.as_view(), name='product_update')

]