from django.contrib import admin

from .models import Question, PeopleCount,Choice

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(PeopleCount)

