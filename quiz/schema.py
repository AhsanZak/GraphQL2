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
    all_questions = graphene.Field(QuestionType, id=graphene.Int())
    all_answers = graphene.List(AnswerType, id=graphene.Int())

    def resolve_all_questions(root, info, id):
        return Question.objects.get(pk=id)
    
    def resolve_all_answers(root, info, id):
        return Answer.objects.filter(question=id)

class CategoryMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name):
        category = Category(name=name)
        category.save()
        return CategoryMutation(category=category)

class CategoryUpdateMutation(graphene.Mutation):

    class Arguments:
        id = graphene.ID()
        name = graphene.String(required=True)

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, name, id):
        category = Category.objects.get(id=id)
        category.name = name
        category.save()
        return CategoryMutation(category=category)

class CategoryDeleteMutation(graphene.Mutation):

    class Arguments:
        id = graphene.ID()

    category = graphene.Field(CategoryType)

    @classmethod
    def mutate(cls, root, info, id):
        category = Category.objects.get(id=id)
        category.delete()
        return
    
class QuizzesMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        category = graphene.String(required=True)

    quiz = graphene.Field(QuizzesType)

    @classmethod
    def mutate(cls, root, info, title, category):
        category_q = Category.objects.get(name=category)
        quiz = Quizzes(title=title, category=category_q)
        quiz.save()
        return QuizzesMutation(quiz=quiz)


class Mutation(graphene.ObjectType):
    update_category = CategoryMutation.Field()
    update_quizzes = QuizzesMutation.Field()
    edit_category = CategoryUpdateMutation.Field()
    delete_category = CategoryDeleteMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)