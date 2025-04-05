from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
from django.template import loader # type: ignore


def members(request):
   template = loader.get_template('myfirst.html ') # type: ignore
   return HttpResponse(template.render()) 
