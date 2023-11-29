from django.urls import path
from relogio.views import index, relogio
from django.http import HttpResponse

urlpatterns = [
    path('', index, name='index'),
    path('relogio/', relogio, name='relogio'),
    
]



