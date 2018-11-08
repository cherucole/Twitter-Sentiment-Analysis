from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$',  views.LineChartJSONView.as_view(), name='line_chart_json'),
    url(r'^analyse/$', views.analyse, name='analyse'),
    url(r'^$', views.index, name='index'),
    # url(r'^pdf/$', views.Pdf.as_view(), name='pdf'),
    # url(r"^(\d+)/$", Pdf.views.BerichtListView.as_view()),
    # url(r'^pdf(\d+)/$', views.Pdf, name='pdf')
    url(r'^query/$', views.analyse, name='query'),
    url(r'^signup/', views.register, name='signup'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^pdf/(?P<username>\w+)', views.get_pdf, name='reports'),
    url(r'^pdf/', views.get_pdf, name='get_pdf'),
]
