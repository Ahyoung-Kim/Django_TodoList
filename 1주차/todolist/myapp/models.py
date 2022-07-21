from django.db import models

# Create your models here.
class Todo(models.Model):
  id = models.AutoField(primary_key=True)
  contents = models.CharField(max_length=300)
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.contents