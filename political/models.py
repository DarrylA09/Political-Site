from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# This class represents the Question model.
# It contains a foreign key to the User model, a text field for the question
# text
class Question(models.Model):
    """
    This class represents the Question model.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text


# This class represents the Event model.
# It contains fields for the city, date, and venue of the event.
class Event(models.Model):
    city = models.CharField(max_length=100)
    date = models.DateField()
    venue = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.city} - {self.date}"
