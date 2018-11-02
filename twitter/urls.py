from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$',  views.LineChartJSONView.as_view(), name='line_chart_json'),
    url(r'^analyse/$', views.analyse, name='analyse'),
    url(r'^$', views.home, name='home')


]
