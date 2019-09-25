from django.urls import path

from tests.views import TestListViews, TestDetalView, TestQuestion, QuestionDetalView

app_name = 'tests'

urlpatterns = [
    path('', TestListViews.as_view(), name='test'),
    path('question/<int:pk>/', TestDetalView.as_view(), name='test_detal'),
    path('answer/<int:pk>/', QuestionDetalView.as_view(), name='question_detal'),
]