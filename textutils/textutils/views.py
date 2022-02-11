# I have created this file - Mohsin

from email.policy import default
import http
from typing import ParamSpecArgs
from django.http import HttpResponse    
from django.shortcuts import render

def home(request):
    params = {'name':'Mohsin', 'place':'Lucknow'}
    return render(request, 'index.html', params)

def charcount(request):
    return HttpResponse("<h1>Character Count</h1> <a href='http://127.0.0.1:8000/'>Back</a>")

def removepunc(request):
    #get text
    djtext = request.GET.get('text', 'default')
    print(djtext)
    #analyze text
    return HttpResponse("<h1>Remove Punctuation</h1> <a href='http://127.0.0.1:8000/'>Back</a>")

def capitalizefirst(request):
    return HttpResponse("<h1>Capitalize First</h1> <a href='http://127.0.0.1:8000/'>Back</a>")

def newlineremover(request):
    return HttpResponse("<h1>New Line Remover</h1> <a href='http://127.0.0.1:8000/'>Back</a>")

def spaceremover(request):
    return HttpResponse("<h1>Space Remover</h1> <a href='http://127.0.0.1:8000/'>Back</a>")