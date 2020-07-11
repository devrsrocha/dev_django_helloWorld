from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome):
    return HttpResponse('<h1>Hello {}</h1>'.format(nome))

def soma(request, n1, n2):
    soma = n1 + n2
    return HttpResponse('<h1>A soma de {} e {} é: {}</h1>'.format(n1, n2, soma))