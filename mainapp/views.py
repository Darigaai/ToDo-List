from django.shortcuts import render
from .models import ToDo
# Create your views here.

def index(request):
    return render(request, 'index.html')

def todo_list(request):
    todos = ToDo.objects.all()
    context = {'todos':todos}
    return render(request, 'todo_list.html', context=context)
