from django.urls import path

from . import views

app_name = "quiz"


urlpatterns = [
    path("api/", views.QuizListView.as_view(), name="quiz"),
]