# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request, username):
    print(username)
    return HttpResponse("<h2> Hello World</h2>")

def about(request):
    return HttpResponse('<p>About<p>')
