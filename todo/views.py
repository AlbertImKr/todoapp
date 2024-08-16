from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Todo
from .serializers import TodoSerializer


class TodoListView(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetailView(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'


class TodoCreateView(generics.CreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoUpdateView(generics.UpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    lookup_field = 'pk'


class TodoCompleteView(APIView):
    def post(self, request, pk):
        try:
            todo = Todo.objects.get(pk=pk)
            todo.is_completed = True
            todo.save()
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Todo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class TodoDeleteView(generics.DestroyAPIView):
    queryset = Todo.objects.all()
    lookup_field = 'pk'
