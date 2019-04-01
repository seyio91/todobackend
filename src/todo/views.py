from django.shortcuts import render

# Create your views here.
from todo.models import TodoItem
from todo.serializers import TodoItemSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.reverse import reverse 
from rest_framework.decorators import list_route
from rest_framework.response import Response

#class inherited from a model viewset class with default
#functionality built in on how to respond to each api request
class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

    def perform_create(self, serializer):
        #Save instance to get primary key then update url
        #construct the url
        #persist updated item
        instance = serializer.save()
        instance.url = reverse('todoitem-detail', args=[instance.pk], request=self.request)
        instance.save()


        # Delete all todo items
    def delete(self, request):
        TodoItem.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
