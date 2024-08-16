from django.urls import path

from .views import TodoDetailView
from .views import TodoListView

urlpatterns = [
    path('todos/', TodoListView.as_view(), name='todo-list'),
    path('todos/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
]
