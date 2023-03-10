from django.db import models
from users.models import Users
from classes.models import Classrooms

# Create your models here.
class Material(models.Model):
    material_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    classroom_id = models.ForeignKey(Classrooms, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    study_material = models.FileField(upload_to="materials/")
    material_title = models.CharField(max_length=250, null=True)

    class Meta:
        db_table = 'study_materials'

