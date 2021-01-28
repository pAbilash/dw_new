from django.db import models

# Create your models here.

class Test(models.Model):
    question_id = models.IntegerField(primary_key=True)
    question_video = models.FileField(upload_to='media')
    question_text = models.CharField(max_length=200)
    answer = models.CharField(max_length=100)
    user_answer = models.CharField(max_length=100,blank=True)
    percentage = models.IntegerField(blank=True)
