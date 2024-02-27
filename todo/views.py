from django.shortcuts import render

from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects  # .all().order_by('-date_joined') 
   
    serializer_class = TodoSerializer
    permission_classes = [] # permissions.IsAuthenticated
