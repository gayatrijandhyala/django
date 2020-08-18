from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('<h1>This is the home page.</h1>')
def about(request):
    return HttpResponse('<h2>I am a CS major and this is me learning django</h2>')
def myhobbies(request):
    return HttpResponse('<h2>I like to code, read books and write my thoughts.</h2>')

