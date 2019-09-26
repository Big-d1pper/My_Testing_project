from django.shortcuts import render
from django.views.generic import CreateView
from tests.models import  Test, TestQuestion, PossibleAnswer
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from tests.forms import TestModelForm, TestQuestionModelForm , AnswerModelForms
from django.contrib import messages
from django.urls import reverse_lazy


class TestListViews(ListView):
    model = Test
    context_object_name = 'my_test'
    template_name = 'index.html'


class TestDetalView(DetailView):
    model = Test
    template_name = 'test_detal.html'

    def get_context_data(self, **kwargs):
        context = super(TestDetalView, self).get_context_data(**kwargs)
        context['question'] = TestQuestion.objects.filter(test=kwargs['object'])
        return context


class QuestionDetalView(DetailView):
    model = TestQuestion
    context_object_name = 'question'
    template_name = 'question_detal.html'

    def get_context_data(self, **kwargs):
        context = super(QuestionDetalView, self).get_context_data(**kwargs)
        context['answer'] = PossibleAnswer.objects.filter(question=kwargs['object'])
        return context


class AnswerDetalView(DetailView):
    model = PossibleAnswer
    context_object_name = 'answer'
    template_name = 'answer.html'


class TestCreateView(CreateView):
    model = Test
    form_class = TestModelForm
    success_url = reverse_lazy("tests:test")
    template_name = 'add_test.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Test has been successfully added.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class QuestionCreateView(CreateView):
    model = TestQuestion
    form_class = TestQuestionModelForm
    success_url = reverse_lazy ("tests:test")
    template_name = 'add_question.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Question has been successfully added.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        return super(QuestionCreateView, self).get(request, *args, **kwargs)

    def get_initial(self, *args, **kwargs):
        return {'test': self.kwargs['test_id']}


class AnswerCreateView(CreateView):
    model = PossibleAnswer
    form_class = AnswerModelForms
    success_url = reverse_lazy("tests:test")
    template_name = 'add_answer.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Answer has been successfully added.')
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        return super(AnswerCreateView, self).get(request, *args, **kwargs)

    def get_initial(self, *args, **kwargs):
        print(self.kwargs['question_id'])
        return {'question': self.kwargs['question_id']}


