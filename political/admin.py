from django.contrib import admin
from .models import Question, Event

# Register your models here.
# This line registers the Question and Event model with the Django admin site.
admin.site.register(Question)
admin.site.register(Event)


# This class customizes the admin interface for the Event model.
class EventAdmin(admin.ModelAdmin):
    list_display = ('city', 'date', 'venue')
    search_fields = ('city', 'venue')
