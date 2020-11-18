''' Blog views '''

from django.shortcuts import render
from django.http import HttpResponse

def blog(request):
    return HttpResponse("This will the Wymco's blog")