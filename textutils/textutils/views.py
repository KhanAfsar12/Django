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

def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps' ,'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    alphabetcounter = request.GET.get('alphabetcounter', 'off')

    # Check which checkbox is on
    if removepunc == 'on':
        punctuations = '''!()-{}[]:;'"\,/<>.?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed += char
        params = {'Purpose': 'remove punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif fullcaps == 'on':
        analyzed = ''
        for char in djtext:
            analyzed += char.upper()
        params = {'Purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif newlineremover == 'on':
        analyzed = ''
        for char in djtext:
            if char != '\n':
                analyzed += char.upper()
        params = {'Purpose': 'Remove New Lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)


    elif extraspaceremover == 'on':
        analyzed = djtext[0]
        for index, char in enumerate(djtext[:-1]):
            if char != " " or djtext[index + 1] != " ":
                analyzed += char
        if djtext[-1] != " ":
            analyzed += djtext[-1]
        params = {'Purpose': 'Extra space remover', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif alphabetcounter == 'on':
        count = 0
        for char in djtext:
            if char != " ":
                count += 1
            else:
                continue
        params = {'Purpose': 'Alphabet counter', 'analyzed_text': count}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('error')