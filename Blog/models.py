from django.db import models
from django.db.models.base import Model
from django.db.models.fields.files import ImageField
from django.urls import reverse
from django.template.defaultfilters import slugify
# Create your models here.
from ckeditor.fields import RichTextField


class Subject(models.Model):
    subject = models.CharField(max_length=250, blank=False, unique=True)

    def __str__(self):
        return self.subject


class Topic(models.Model):
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=250, blank=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Topic_view", kwargs={"topic_id": self.id})


class Content(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    sub_title = models.CharField(max_length=250, blank=False)
    content = models.TextField(max_length=5000, blank=False)
    # image = models.ImageField(upload_to='Post')
    published_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.sub_title

    def get_absolute_url(self):
        return reverse("blog", kwargs={"blog_id": self.id})


class TestModel(models.Model):
    image = models.ImageField(upload_to='Post')
    description = RichTextField(blank=True, null=True)
