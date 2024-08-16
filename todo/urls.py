from django.urls import path

from .views import TodoCompleteView
from .views import TodoCreateView
from .views import TodoDeleteView
from .views import TodoDetailView
from .views import TodoListView
from .views import TodoUpdateView
from .views import todo_list
from .views import todo_complete
from .views import todo_delete

urlpatterns = [
    path('todos/', TodoListView.as_view(), name='todo-list'),
    path('todos/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('todos/create/', TodoCreateView.as_view(), name='todo-create'),
    path('todos/<int:pk>/update/', TodoUpdateView.as_view(),
         name='todo-update'),
    path('todos/<int:pk>/complete/', TodoCompleteView.as_view(),
         name='todo-complete'),
    path('todos/<int:pk>/delete/', TodoDeleteView.as_view(),
         name='todo-delete'),
    path('', todo_list, name='todo-list'),
    path('complete/<int:pk>/', todo_complete, name='todo-complete'),
    path('delete/<int:pk>/', todo_delete, name='todo-delete'),
]
