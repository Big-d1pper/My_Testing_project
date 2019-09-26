from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=100)
    # question = models.ManyToManyField('tests.TestQuestion', null=True, blank=True)

    def __str__(self):
        return self.name


class TestQuestion(models.Model):
    question = models.CharField(max_length=100)
    test = models.ForeignKey('tests.Test', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class PossibleAnswer(models.Model):
    question = models.ForeignKey('tests.TestQuestion', null=True, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100)
    try_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.answer

