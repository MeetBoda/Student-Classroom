from django.contrib import admin
from answer.models import Answers

# Register your models here.
class AnswerAdmin(admin.ModelAdmin):
    list_display=('user_id', 'ans', 'classroom_id', 'doubt_id')

admin.site.register(Answers, AnswerAdmin)