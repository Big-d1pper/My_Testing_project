from django.urls import path
from django.conf.urls import url

from tests.views import TestListViews, TestDetalView, TestQuestion, QuestionDetalView, TestCreateView, QuestionCreateView, AnswerDetalView, AnswerCreateView

app_name = 'tests'

urlpatterns = [
    path('', TestListViews.as_view(), name='test'),
    path('test_detal/<int:pk>/', TestDetalView.as_view(), name='test_detal'),
    path('answer/<int:pk>/', QuestionDetalView.as_view(), name='question_detal'),
    path('answer_dital/<int:pk>/', AnswerDetalView.as_view(), name='answer'),
    path('add_test/', TestCreateView.as_view(), name='add_test'),
    url(r'^add_question/(?P<test_id>\w+)/$', QuestionCreateView.as_view(), name='add_question'),
    url(r'^add_answer/(?P<question_id>\w+)/$', AnswerCreateView.as_view(), name='addanswer')

]