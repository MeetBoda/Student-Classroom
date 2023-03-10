from django.db import models
from classes.models import Users, Classrooms

# Create your models here.

class Doubts(models.Model):
    doubt_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    classroom_id = models.ForeignKey(Classrooms, on_delete=models.CASCADE)
    question = models.TextField()

    class Meta:
        db_table = 'doubts'
