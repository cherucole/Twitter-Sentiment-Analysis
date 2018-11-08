from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$',  views.LineChartJSONView.as_view(), name='line_chart_json'),
    url(r'^analyse/$', views.analyse, name='analyse'),
    url(r'^$', views.index, name='index'),
    url(r'^query/$', views.analyse, name='query'),
    url(r'^signup/', views.register, name='signup'),
    url(r'^user/(?P<username>\w+)', views.profile, name='profile'),
    url(r'^history/(?P<username>\w+)', views.profilehistory, name='history'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^pdf/(?P<username>\w+)', views.get_pdf, name='reports'),
    url(r'^pdf/', views.get_pdf, name='get_pdf'),
    url(r'^csv/$', views.export_users_csv, name='export_csv'),
    url(r'^privacy/$', views.privacy, name='privacy'),
]
