from django.http.response import Http404
from django.shortcuts import render, HttpResponse, get_object_or_404
from . models import Content, Topic
# Create your views here.


def Home(request):
    title = []
    sub_title = []
    for item in Topic.objects.all():
        title.append(item)
        sub_title.append(Content.objects.filter(topic__title=item))

    # print((title))
    # print((sub_title))

    context = {
        'Contents': Content.objects.all(),
        'titles': title,
        'sub_titles': sub_title,
    }
    return render(request, 'Blog/index.html', context)


def Blog(request, blog_id):
    try:
        blog = get_object_or_404(Content, id=blog_id)
    except:
        return render(request, 'Blog/Pagenotfound.html')
    context = {
        'Blog': blog
    }
    return render(request, 'Blog/Blog.html', context)


def Topic_view(request, topic_id):
    # Contents = []
    title = []
    sub_title = []
    for item in Topic.objects.all():
        title.append(item)
        sub_title.append(Content.objects.filter(topic__title=item))

    try:
        item = get_object_or_404(Topic, id=topic_id)
    except:
        return render(request, 'Blog/Pagenotfound.html')
    Contents = Content.objects.filter(topic=item)

    context = {
        'titles': title,
        'sub_titles': sub_title,
        "Contents": Contents
    }
    if len(Contents) <= 0:
        return render(request, 'Blog/Notopic.html', context)
    return render(request, 'Blog/Topic.html', context)
