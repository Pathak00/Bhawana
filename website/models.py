from django.db import models
import datetime

# Create your models here.
class Poem(models.Model):
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=50)
    date = models.DateField()
    poem_text=  models.TextField()

    
    def __str__(self):
        # my_date=datetime.self.date
        return f"{self.title} {self.writer} {self.date.strftime('%Y-%m-%d')} {self.poem_text}" 