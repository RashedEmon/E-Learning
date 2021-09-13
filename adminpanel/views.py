
from django.urls import reverse
from django.http import response
from django.core import serializers
from django.http.response import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.db import IntegrityError
from django.contrib.auth import logout, authenticate, login


from Blog.models import Subject, Topic, Content
from django.contrib.auth.models import User
# Create your views here.


def paginator_assist(paginator, single_page, max_num_of_link):
    import math
    link_number = []
    if paginator.num_pages <= max_num_of_link:
        link_number = [i for i in range(1, paginator.num_pages+1)]
    else:
        if single_page.number > math.floor(max_num_of_link/2):
            for i in range(single_page.number-math.floor(max_num_of_link/2), single_page.number+math.ceil(max_num_of_link/2)):
                if i <= paginator.num_pages:
                    link_number.append(i)

        else:
            link_number = [i for i in range(1, max_num_of_link)]
    return link_number


def index(request):
    if request.method == 'GET':

        post = Content.objects.order_by('published_date')

        return render(request, 'home.html', {'num_of_user': User.objects.count(), 'num_of_post': Content.objects.count(), 'subjects': Subject.objects.all(), 'posts': post.reverse()[:5]})

    if request.method == 'POST':
        print("POST request")
        content = request.POST['editor']
        return HttpResponse(f"<h1>{content}</h1>")


def add_subject(request):
    if request.method == 'POST':
        context = {}
        subject_name = request.POST['subject']

        try:
            Subject.objects.create(subject=subject_name.lower())
            request.session["add_sub_noti"] = "{subject_name} added successfully"
        except IntegrityError:
            print(f"Subject {subject_name} already exist")
            request.session["duplicate_data_error"] = f"{subject_name} already Exist"
        return redirect(reverse('subject-list'))

    if request.method == 'GET':
        return redirect(reverse('subject-list'))


def Subject_List_View(request):
    num_of_page = 5
    max_num_of_link = 5
    link_number = []
    subject_list = Subject.objects.all()
    paginator = Paginator(subject_list, num_of_page)
    page_number = request.GET.get('page')
    single_page = paginator.get_page(page_number)
    i = (single_page.number-1)*num_of_page

    print(link_number)
    context = {
        'single_page': single_page,
        'i': i,
        'link_number': paginator_assist(paginator, single_page, max_num_of_link)
    }
    return render(request, 'categories.html', context)


def topic_list_by_subject_view(request, *args, **kwargs):
    if request.method == "GET":
        subject_name = request.GET['subject'].lower()

        topiclist = Topic.objects.filter(
            subject__subject__contains=subject_name)
        print(topiclist)
        topiclist = serializers.serialize('json', topiclist)
        return HttpResponse(topiclist)


def add_topic_view(request):
    if request.method == 'POST':

        subject = request.POST.get('subject', False)
        new_topic = request.POST.get('topic', False)
        try:
            new_subject = Subject.objects.get(pk=subject)
        except:
            return HttpResponse("subject doesn't exist")
        Topic.objects.create(subject=new_subject, title=new_topic)

        return HttpResponse("successfully saved")
    return HttpResponse('only post request acceptable')


def add_post_view(request):
    print(request.POST)
    title = request.POST['title']
    subject = request.POST['subject']
    topic = request.POST['topic']
    content = request.POST['editor']

    try:
        topic = Topic.objects.get(pk=topic)
        subject = Subject.objects.get(pk=subject)
    except:
        return redirect('/admin',)

    Content.objects.create(topic=topic, subject=subject,
                           sub_title=title, content=content)
    return redirect('/admin')


def user_list_view(request):
    return render(request, 'users.html', {})


def login(request):
    pass


def Logout(request):
    logout(request)
    return redirect('/', permanent=True)
    
