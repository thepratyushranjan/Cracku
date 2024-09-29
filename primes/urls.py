
from django.urls import path
from . import views

urlpatterns = [
    path('', views.prime_numbers_view, name='prime_numbers'),
]
