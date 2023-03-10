from django.contrib import admin
from material.models import Material

# Register your models here.
class MaterialAdmin(admin.ModelAdmin):
    list_display=('user_id', 'study_material', 'classroom_id', 'date', 'material_title')

admin.site.register(Material, MaterialAdmin)