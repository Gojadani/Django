from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def testIndex(request):
    return HttpResponse("Hello, World!")