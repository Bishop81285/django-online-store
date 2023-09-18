from django.urls import path

from main.views import home, contacts

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]
