from django.contrib import admin

from webapp.models import Poll, Choice


class PollAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'created_at']
    list_filter = ['question']
    fields = ['question']


admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)