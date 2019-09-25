from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=100)
    question = models.ManyToManyField('tests.TestQuestion')

    def __str__(self):
        return self.name


class TestQuestion(models.Model):
    question = models.CharField(max_length=100)
    answer = models.ManyToManyField('tests.PossibleAnswer')

    def __str__(self):
        return self.question


class PossibleAnswer(models.Model):
    answer = models.CharField(max_length=100)
    try_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.answer

