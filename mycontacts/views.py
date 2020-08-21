from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def whoami(requests):
    return HttpResponse('I am a IT major student coding django website.')
