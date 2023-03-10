from django.db import models
from users.models import Users
# Create your models here.

class Classrooms(models.Model):
    classroom_id = models.AutoField(primary_key=True)
    classroom_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'classrooms'

class Persons(models.Model):
    user_id = models.ForeignKey(Users, null=False, on_delete=models.CASCADE, related_name="user_id_copy")
    role = models.ForeignKey(Users, null=False, on_delete=models.CASCADE)
    classroom_id = models.ForeignKey(Classrooms, on_delete=models.CASCADE)

    class Meta:
        db_table = 'persons'