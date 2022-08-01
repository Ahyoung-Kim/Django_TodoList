from email.policy import default
from django.db import models

class CurrDate(models.Model):
  id = models.AutoField(primary_key=True)
  year = models.IntegerField()
  month = models.IntegerField()
  date = models.IntegerField()
  cnt = models.IntegerField(default=0)

# Create your models here.
class Todo(models.Model):
  id = models.AutoField(primary_key=True)
  contents = models.CharField(max_length=300)
  complete = models.BooleanField(default=False)
  edit = models.BooleanField(default=False)
  date = models.DateTimeField(auto_now_add=True)
  day = models.ForeignKey(CurrDate, null=True, blank=True, on_delete=models.CASCADE)

  def __str__(self):
    return self.contents