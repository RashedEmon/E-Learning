from django.contrib import admin
from . models import Topic, Content, Subject, TestModel
# Register your models here.
# admin.site.register(Topic)
# admin.site.register(Content)
# admin.site.register(Subject)
# admin.site.register(TestModel)


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject']
    list_filter = ['title']
    search_fields = ['title', 'subject']

    class Meta:
        model = Topic


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['subject']
    list_filter = ['subject']
    search_fields = ['subject']

    class Meta:
        model = Subject


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'topic', 'sub_title', 'published_date']
    list_filter = ['subject', 'topic']
    search_fields = ['subject', 'topic']
    date_hierarchy = 'published_date'
    ordering = ['subject']

    class Meta:
        model = Content
