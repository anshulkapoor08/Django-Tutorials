from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore

def members(request):
   return HttpResponse("Hello, this is the members page!") 
