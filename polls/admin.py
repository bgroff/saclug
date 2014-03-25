from django.contrib import admin
from polls.models import Poll, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    exclude = ('votes',)


class PollAdmin(admin.ModelAdmin):
    inlines = [
        ChoiceInline,
    ]
    exclude = ('pub_date',)

admin.site.register(Poll, PollAdmin)
