from django.contrib import admin
from doubt.models import Doubts

# Register your models here.
class DoubtAdmin(admin.ModelAdmin):
    list_display=('user_id', 'question', 'classroom_id')

admin.site.register(Doubts, DoubtAdmin)