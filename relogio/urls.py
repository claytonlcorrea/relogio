from django.urls import path
from relogio.views import index, relogio

urlpatterns = [
    path('', index),
    path('relogio/', relogio)
]
