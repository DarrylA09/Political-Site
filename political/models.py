from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    """
    This class represents a question asked by a user.
    It contains a foreign key to the User model, a text field for the question
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text


class Event(models.Model):
    """
    This class represents an event in the political context.
    It contains fields for the city, date, and venue of the event.
    """
    city = models.CharField(max_length=100)
    date = models.DateField()
    venue = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.city} - {self.date}"
