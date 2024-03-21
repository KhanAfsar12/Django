# i have created this file
from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse('<h1>Hello Wolrd</h1><a href = "https://docs.google.com/document/d/196xS4AuS9GPhy6jMsnph9Awbu4SQKTHEEql55ZL4Xwc/edit">Falsk Road Map</a>')
#
# def about(request):
#     return HttpResponse("Welcome")

from django.http import HttpResponse
def index(request):
    dict = {'name':'Afsar', 'country':'india'}
    return render(request, 'index.html', dict)

def removepunc(request):
    print(request.GET.get('text', 'default'))
    return HttpResponse('remove punc')