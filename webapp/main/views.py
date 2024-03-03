from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView


def index(request):
    # return HttpResponse("<y4> Проверка работы </h4>")
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    # return HttpResponse("<y4> Страница про нас </h4>")
    return render(request, 'main/about.html')

