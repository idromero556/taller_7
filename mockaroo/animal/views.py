import json

import requests
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from animal.models import Animal


def index(request):
    url = "https://my.api.mockaroo.com/animal_favorito.json?pais=Colombia&key=e66a4260"
    try:
        result = requests.get(url)
        print(result.content)
        animales = json.loads(result.content, encoding='utf-8')
        print(animales)
        for a in animales:
            mockis = Animal.objects.create(
                nombres = a['nombres'],
                apellido = a['apellido'],
                email = a['email'],
                genero = a['genero'],
                pais = a['pais'],
                animal = a['animal favorito'],
            )
            mockis.save()
        return HttpResponse('ok')
    except Exception as e:
        print(e)
        return HttpResponse('error')
