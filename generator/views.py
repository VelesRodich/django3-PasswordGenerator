from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')


def password(request):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    rus_letters = 'абвгдеёжзиклмнопрстуфхцчшщыэюя'
    special = '!@#$%^&*()_+=-'
    nubmbers = '1234567890'

    characters = list(letters)

    if request.GET.get('русский'):
        letters = rus_letters
        characters = list(letters)
        
    if request.GET.get('uppercase'):
        characters.extend(list(letters.upper()))

    if request.GET.get('special'):
        characters.extend(list(special))

    if request.GET.get('numbers'):
        characters.extend(list(nubmbers))

    length = int(request.GET.get('length', 12))

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})
