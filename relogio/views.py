from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def relogio(request):
    agora = datetime.now()
    hora_atual = agora.strftime("%H:%M")

    imagens_de_fundo = {
        "01:00-01:59": "img/01h.png",
        "02:00-02:59": "img/02h.png",
        "03:00-03:59": "img/03h.png",
        "04:00-04:59": "img/04h.png",
        "05:00-05:59": "img/05h.png",
        "06:00-06:59": "img/06h.png",
        "07:00-07:59": "img/07h.png",
        "08:00-09:30": "img/08h.png",
        "09:31-09:59": "img/09h.png",
        "10:00-11:29": "img/10h.png",
        "11:30-11:59": "img/11h.png",
        "12:00-12:59": "img/12h.png",
        "13:00-13:30": "img/13h.png",
        "13:31-16:59": "img/14h.png",
        "17:00-17:59": "img/17h.png",
        "18:00-19:59": "img/18h.png",
        "20:00-20:59": "img/20h.png",
        "21:00-21:59": "img/21h.png",
        "22:00-00:59": "img/23h.png"
        # Adicione mais intervalos de tempo e imagens conforme necessário
    }

    imagem_fundo = None

    for intervalo, imagem in imagens_de_fundo.items():
        horas_inicio, horas_fim = intervalo.split("-")
        if horas_inicio <= hora_atual <= horas_fim:
            imagem_fundo = imagem
            break
    return render(request, 'relogio.html', {'hora_atual': hora_atual, 'imagem_fundo': imagem_fundo})

def index(request):
    agora = datetime.now()
    hora_atual = agora.strftime("%H:%M")
    return render(request, 'index.html', {'hora_atual': hora_atual})

