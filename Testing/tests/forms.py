from django import forms
from tests.models import Test, TestQuestion, PossibleAnswer


class TestModelForm(forms.ModelForm):
    class Meta:
        model = Test
        exclude = []


class TestQuestionModelForm(forms.ModelForm):
    class Meta:
        model = TestQuestion
        exclude = []


class AnswerModelForms(forms.ModelForm):
    class Meta:
        model = PossibleAnswer
        exclude = []
