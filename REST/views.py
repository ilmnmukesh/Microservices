from django.shortcuts import render
from rest_framework import viewsets
from .serializer import BookSerializer
from .models import Books

class BookViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BookSerializer