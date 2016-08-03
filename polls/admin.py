from django.contrib import admin

# Register your models here.
from .models import Questions,Choices

class ChoicesInLine(admin.TabularInline):
    model = Choices
    extra = 3

class QuestionsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    inlines = [ChoicesInLine]

    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ('pub_date',)
    search_fields = ('question_text',)


admin.site.register(Questions,QuestionsAdmin)
admin.site.register(Choices)