from django.contrib import admin
from .models import Question, Event

# Register your models here.
# This line registers the Question and Event model with the Django admin site.
admin.site.register(Question)
admin.site.register(Event)


# This class customizes the admin interface for the Event model.
class EventAdmin(admin.ModelAdmin):
    """
    This class customizes the admin interface for the Event model.
    
    :class EventAdmin(admin.ModelAdmin):
    :param list_display: A tuple of field names to display in the admin list view.
    :type list_display: tuple
    :param search_fields: A tuple of field names to enable search functionality in the admin interface.
    :type search_fields: tuple
    :return: None
    :rtype: None
    """
    list_display = ('city', 'date', 'venue')
    search_fields = ('city', 'venue')
