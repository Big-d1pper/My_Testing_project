from django.contrib import admin
from tests.models import Test, PossibleAnswer, TestQuestion


admin.site.register(Test)
admin.site.register(PossibleAnswer)
admin.site.register(TestQuestion)