from django.shortcuts import render
from tests.models import  Test, TestQuestion, PossibleAnswer
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class TestListViews(ListView):
    model = Test
    context_object_name = 'my_test'
    template_name = 'index.html'


class TestDetalView(DetailView):
    model = Test
    template_name = 'test_detal.html'


class QuestionDetalView(DetailView):
    model = TestQuestion
    context_object_name = 'question'
    template_name = 'question_detal.html'