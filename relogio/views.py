from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'index.html')

def relogio(request):
    agora = datetime.now()
    hora_atual = agora.strftime("%H:%M")

    imagens_de_fundo = {
        "01:01-02:00": "img/01h.png",
        "02:01-03:00": "img/02h.png",
        "03:01-04:00": "img/03h.png",
        "04:01-05:00": "img/04h.png",
        "05:01-06:00": "img/05h.png",
        "06:01-07:00": "img/06h.png",
        "07:01-08:00": "img/07h.png",
        "08:01-09:00": "img/08h.png",
        "09:01-10:00": "img/09h.png",
        "10:01-11:30": "img/10h.png",
        "11:31-12:30": "img/11_30h.png",
        "12:31-17:00": "img/14h.png",
        "17:01-18:00": "img/17h.png",
        "18:01-20:00": "img/01h.png",
        "20:01-21:00": "img/20hh.png",
        "21:01-22:00": "img/21h.png",
        "22:01-01:00": "img/23h.png"
        # Adicione mais intervalos de tempo e imagens conforme necessário
    }

    imagem_fundo = None

    for intervalo, imagem in imagens_de_fundo.items():
        horas_inicio, horas_fim = intervalo.split("-")
        if horas_inicio <= hora_atual <= horas_fim:
            imagem_fundo = imagem
            break
    return render(request, 'relogio.html', {'hora_atual': hora_atual, 'imagem_fundo': imagem_fundo})
