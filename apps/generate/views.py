from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    context = {
        'rand_string': get_random_string(length = 12)
    }
    return render(request, 'generate/index.html', context) 

def click(request):
    return redirect('/')