from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Task

import json

# Create your views here.


def admin_view(request):
    template = loader.get_template('admin_bot/index.html')
    context = {
        'tasks': Task.objects.all(),
    }
    return HttpResponse(template.render(context, request))
    
def action_view(request):
    data = { "tasks": Task.objects.all() }
    params = json.loads(request.body)
    
    b = Task(text=params["action"], result=False, login=params['login'], 
        password=params["password"], link=params["link"])
    b.save()
        
    return HttpResponse(data, content_type='application/json')
