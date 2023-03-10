from django.contrib import admin
from classes.models import Classrooms, Persons

class ClassAdmin(admin.ModelAdmin):
    list_display=('classroom_name',)

admin.site.register(Classrooms, ClassAdmin)

class PersonAdmin(admin.ModelAdmin):
    list_display=('user_id', 'role', 'classroom_id')

admin.site.register(Persons, PersonAdmin)
# Register your models here.
