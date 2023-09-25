import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from .models import Quizzes, Category, Question, Answer

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ("id", "name")


class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        feilds = ("id", "title", "category", "quiz")

    
class QuestionType(DjangoObjectType):
    class Meta:
        model = Question
        fields = ("title", "quiz")

    
class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        feilds = ("question", "answer_text")


class Query(graphene.ObjectType):
    all_quizzes = graphene.Field(QuizzesType, id=graphene.Int())

    def resolve_all_quizzes(root, info, id):
        return Quizzes.objects.get(pk=id)

schema = graphene.Schema(query=Query)