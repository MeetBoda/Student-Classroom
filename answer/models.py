from django.db import models
from doubt.models import Doubts
from classes.models import Classrooms
from users.models import Users

# Create your models here.
class Answers(models.Model):
    answer_id = models.AutoField(primary_key=True)
    doubt_id = models.ForeignKey(Doubts, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    classroom_id = models.ForeignKey(Classrooms, on_delete=models.CASCADE)
    ans = models.TextField()

    class Meta:
        db_table = 'answers'
        