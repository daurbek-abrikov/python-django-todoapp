import re
from django.shortcuts import render
from .models import Category, Todo
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
    return render(request, 'blog/home.html')

@login_required
def todo(request):
    context = {
        'todos': Todo.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request, 'blog/todo.html', context)

class TodoListView(ListView):
    model = Todo
    template_name = 'blog/todo.html'
    context_object_name = 'todos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todos'] = context['todos'].filter(author=self.request.user)
        return context

class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['title', 'comment', 'category', 'due_date']
    success_url = '/todo/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TodoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Todo
    fields = ['title', 'comment', 'category', 'due_date']
    success_url = '/todo/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.author:
            return True
        return False

class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Todo
    success_url = '/todo/'
    
    def test_func(self):
        todo = self.get_object()
        if self.request.user == todo.author:
            return True
        return False 