from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello, Welcome to home page..")

def aboutpage(request):
    return HttpResponse("Hello, My name is Harshil Padhiyar.")

def contactpage(request):
    return HttpResponse("Contact me page..")
