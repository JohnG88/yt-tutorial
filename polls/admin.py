from django.contrib import admin
from .models import Question, Choice
# Register your models here.

# This created just a question model
# Idk if you have to add model name and Inline as below like ChoiceInline
# TubularInline creates the admin like:
    # choice text    votes    and an x to delete
# The extra = 3, creates three slots to be filled out
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# The first element of each tuple in fieldsets is the title of the fieldset. Here's what our form looks like now:
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    # Produces in Question in admin: Question text,  Date Published, Was Published Recently
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # This adds a filter sidebar that lets people filter the cahnge list by the pub_date field:
    list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)



