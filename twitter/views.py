from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import userinput
from . apicall import getdata
from chartjs.views.lines import BaseLineChartView
from . models import *
from .utils import render_to_pdf  # created in step 4
from django.template.loader import get_template
import csv


import datetime
from django.contrib.auth.decorators import login_required


# Importations for PDF report processing
from django.views.generic import View
from django.utils import timezone
from .models import *
# from .render import Render
# End of importations for PDF

from .forms import *
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
# Create your views here.


def index(request):

    return render(request, 'index.html')


@login_required(login_url='/login/')
def dashboard(request):

    return render(request, 'dashboard.html')


def privacy(request):

    return render(request, 'privacy.html')


def query(request):
    # hall = 'trump'
    # random = getdata(hall)
    # print(random)
    word = "word of the home"
    return render(request, 'home.html', {"word": word})


@login_required(login_url='/login/')
def analyse(request):
    current_user = request.user

    user_input = userinput(request.GET or None)
    if request.GET and user_input.is_valid():
        input_hastag = user_input.cleaned_data['q']
        data = getdata(input_hastag)
        print(data)
        topic = '#' + data['Topic']
        sample = data['Sample']
        positive = data['Positive']
        neutral = data['Neutral']
        negative = data['Negative']
        negative_tweets = data['Negative_tweets'][0:5]
        negative_tweets1 = len(data['Negative_tweets'])

        neutral_tweets = data['Neutral_tweets'][0:5]
        neutral_tweets1 = len(data['Neutral_tweets'])

        postive_tweets = data['Postive_tweets'][0:5]
        postive_tweets1 = len(data['Postive_tweets'])

        total_positive = len(postive_tweets)
        total_neutral = len(neutral_tweets)

        total_negative = len(negative_tweets)

        # time_positive = data['time_positive']

        # listt = time_positive.keys()
        # print(min(listt))
        sentiments = SentimentsTwitterHashtag(topic=topic,
                                              sample_size=sample,
                                              postive_count=positive,
                                              neutral_count=neutral,
                                              negative_count=negative,
                                              negative_tweets=negative_tweets,
                                              neutral_tweets=neutral_tweets,
                                              postive_tweets=postive_tweets,
                                              publication_date=datetime.datetime.now(),
                                              user=current_user
                                              )
        sentiments.save()
        return render(request, "dashboard.html", {'data': data, 'topic': topic, 'total': sample, 'positive': positive, 'total_positive': postive_tweets1,  'total_neutral': neutral_tweets1, 'total_negative': negative_tweets1,  'sample': sample, 'neutral': neutral, 'negative': negative, 'negative_tweets': negative_tweets, 'neutral_tweets': neutral_tweets, 'postive_tweets': postive_tweets})
    return render(request, "search.html", {'input_hastag': user_input})


# Authentication views
def register(request):
    if request.user.is_authenticated():
        return redirect('index')
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()

            return redirect('auth_login')

        else:
            form = RegistrationForm()
        return render(request, 'registration/signup.html', {'form': form})


def profilehistory(request, username):
    profile = User.objects.get(username=username)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    sentiments = SentimentsTwitterHashtag.get_profile_reports(profile.id)[
        0:5]

    title = f'@{profile.username} Projects'

    return render(request, 'history.html', {'title': title, 'profile': profile, 'sentiments': sentiments, 'profile_details': profile_details})


def profile(request, username):
    profile = User.objects.get(username=username)
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    sentiments = SentimentsTwitterHashtag.get_profile_reports(profile.id)
    title = f'@{profile.username} Projects'

    return render(request, 'profile/profile.html', {'title': title, 'profile': profile, 'sentiments': sentiments, 'profile_details': profile_details})


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            return redirect('profile', username=request.user)
    else:
        form = EditProfileForm()

    return render(request, 'profile/edit_profile.html', {'form': form})


@login_required(login_url='/login/')
def get_pdf(request, username, *args, **kwargs):
    template = get_template('pdf/reports.html')
    profile = User.objects.get(username=username)
    sentiments = SentimentsTwitterHashtag.get_profile_reports(profile.id)

    inv = 'test invoice id to render content'
    context = {
        "invoice_id": inv,
        "sentiments": sentiments,
        'profile': profile,
        "amount": 1399.99,
        "today": "Today",
    }
    html = template.render(context)
    pdf = render_to_pdf('pdf/reports.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Reports_%s.pdf" % ("12341231")
        content = "inline; filename='%s'" % (filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")


def export_users_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reports.csv"'

    writer = csv.writer(response)
    writer.writerow(['Topic', 'Sample size', 'Postive count', 'Neutral count',
                     'Negative count', 'Neutral tweets', 'Negative tweets', 'Postive tweets'])

    reports = SentimentsTwitterHashtag.objects.all().values_list('topic', 'sample_size', 'postive_count',
                                                                 'neutral_count', 'negative_count', 'neutral_tweets', 'negative_tweets', 'postive_tweets')
    for report in reports:
        writer.writerow(report)

    return response
