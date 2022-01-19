from django.urls import path  
from .views import TodoDeleteView, TodoListView, TodoCreateView, TodoUpdateView
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('todo/', TodoListView.as_view(), name='blog-todo'),
    path('todo/new/', TodoCreateView.as_view(), name='todo-create'),
    path('todo/<int:pk>/update/', TodoUpdateView.as_view(), name='todo-update'),
    path('todo/<int:pk>/delete/', TodoDeleteView.as_view(), name='todo-delete'),
]