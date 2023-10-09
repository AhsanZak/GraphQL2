from django.shortcuts import render
from rest_framework import generics

from . import models
from .models import Quizzes
from .serializers import CategorySerializer, QuizzesSerializer


class QuizListView(generics.ListAPIView):
    queryset = Quizzes.objects.all()
    serializer_class = QuizzesSerializer
