from django.db import models
from django import forms
from django.forms.widgets import DateTimeBaseInput
from django.contrib.auth.models import User
# Create your models here.
class Memory(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField( max_length=50)
    desc = models.TextField()
    createOn = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.title

class MemoryForm(forms.ModelForm):
    class Meta:
        model = Memory
        fields = [
            'title',
            'desc',
        ]