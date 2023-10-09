from rest_framework import serializers

from .models import Quizzes, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class QuizzesSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Quizzes
        fields = ["category", "title", "date_created"]
