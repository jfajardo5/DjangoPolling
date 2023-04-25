from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    """
    'fieldsets' sets the display order of the specified columns
    in the admin panel, and splits them into their own segments.
    """
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]

    """
    'list_display' sets the fields to be displayed in the list view for this model.
    """
    list_display = ["question_text", "pub_date", "was_published_recently"]

    """
    'list_filter' adds a sidebar with sorting options in relation to 'pub_date' in the list view.
    """
    list_filter = ["pub_date"]

    """
    'search_fields' adds a search bar to find matches for 'question_text' in the list view.
    """
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)
