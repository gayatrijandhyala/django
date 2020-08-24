from django.shortcuts import render
import operator
from django.http import HttpResponse

# Create your views here.
def wchomepage(requests):
    return render(requests,'wordcount/homepage.html')

def count(requests):
    mytext=requests.GET['FullText']
    wc=mytext.split(" ")
    di=dict()
    for word in wc:
        di[word]=di.get(word,0)+1
    return render(requests,'wordcount/count.html', {'Words':di})
