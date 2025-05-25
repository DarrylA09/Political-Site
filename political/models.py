from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Question(models.Model):
    """
    This class represents a question asked by a user.
    It contains a foreign key to the User model, a text field for the question

    :class Question(models.Model):
    :param user: Foreign key to the User model, representing the user who asked the question.
    :type user: ForeignKey
    :param question_text: Text field for the question content.
    :type question_text: TextField
    :param created_at: DateTime field that automatically sets the time when the question was created.
    :type created_at: DateTimeField
    :return: String representation of the question text.
    :rtype: str
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

    :class Event(models.Model):
    :param city: CharField for the city where the event is held.
    :type city: CharField
    :param date: DateField for the date of the event.
    :type date: DateField
    :param venue: CharField for the venue of the event.
    :type venue: CharField
    :return: String representation of the event in the format "City - Date".
    :rtype: str
    """
    city = models.CharField(max_length=100)
    date = models.DateField()
    venue = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.city} - {self.date}"
