from django.shortcuts import render

from rest_framework import viewsets

from .models import *
from .serializers import *


# Create your views here.

class status_all_view(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = statusSerializer

class child_all_view(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = childSerializer