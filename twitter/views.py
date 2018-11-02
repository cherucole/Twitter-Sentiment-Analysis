from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .forms import userinput
from . apicall import getdata
from chartjs.views.lines import BaseLineChartView


# Create your views here.


def home(request):
    # hall = 'trump'
    # random = getdata(hall)
    # print(random)
    word = "word of the home"
    return render(request, 'home.html', {"word": word})


# class LineChartJSONView(BaseLineChartView):
#     template_name = 'home.html'

#     def get_labels(self):
#         """Return 7 labels for the x-axis."""
#         return ["January", "February", "March", "April", "May", "June", "July"]

#     def get_providers(self):
#         """Return names of datasets."""
#         return ["Central", "Eastside", "Westside"]

#     def get_data(self):
#         """Return 3 datasets to plot."""

#         return [[75, 44, 92, 11, 44, 95, 35],
#                 [41, 92, 18, 3, 73, 87, 92],
#                 [87, 21, 94, 3, 90, 13, 65]]


def analyse(request):
    user_input = userinput(request.GET or None)
    if request.GET and user_input.is_valid():
        input_hastag = user_input.cleaned_data['q']
        # print(input_hastag)
        data = getdata(input_hastag)
        positive = data['Positive']
        neutral = data['Neutral']
        negative = data['Negative']
        nagative_tweets = data['Nagative_tweets'][0:3]
        neutral_tweets = data['Neutral_tweets']
        postive_tweets = data['Postive_tweets']
        print(data['Positive'])
        print(nagative_tweets)
        print(data)
        return render(request, "results.html", {'data': data, 'positive': positive, 'neutral': neutral, 'negative': negative, 'nagative_tweets': nagative_tweets, 'neutral_tweets': neutral_tweets, 'postive_tweets': postive_tweets})
    return render(request, "home.html", {'input_hastag': user_input})
