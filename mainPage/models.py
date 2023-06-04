from django.db import models

# Create your models here.


class QuestionModel(models.Model):
    question_text = models.TextField(max_length=500, primary_key=True)
    uname = models.CharField(max_length=128)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=128)
    
