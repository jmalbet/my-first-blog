from django.shortcuts import render

# Create your views here.

from django.views.generic import View
from django.template.response import TemplateResponse
from todo.models import Todo

class TodoListView(View):
    def get(self, request,_args, _*kwargs):
        context = {
            'todo_list': Todo.objects.all()
        }
        return TemplateResponse(request, 'todo_list.html', context)