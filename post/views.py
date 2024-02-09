'''
views.py - файл, содержащий описание представлений приложения

Методы запроса:
GET - получение данных
POST - отправка данных
PUT - обновление данных
DELETE - удаление данных
'''
import random

from django.shortcuts import render
from django.http import HttpResponse


def test_view(request):
    rn = random.randint(1, 1000)
    return HttpResponse(f'Hello, world! {rn}')


def main_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    