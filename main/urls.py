from django.urls import path

from main.views import index, contacts, product

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contacts, name='contacts'),
    path('product/<int:pk>/', product, name='product')
]
