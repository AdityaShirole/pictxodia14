from django.conf.urls import patterns, url
#from django.views.generic import 
from django.views.generic.base import TemplateView
from bots import views

urlpatterns = patterns('', 
    (r'^$', views.bots_home),
    (r'^(?P<opt>\d+)$', views.bots_home),
    (r'^(?P<first>\d+)vs(?P<second>\d+)/$', views.games),
    #(r'^new-author/add-bot/$', views.add_bot) 
    (r'^sign-up/$', views.sign_up),
    (r'^log-in/$', views.log_in),
    (r'^submit-bot/$', views.submit_bot),
    (r'^log-out/$', views.log_out),
    (r'^leaderboard/$', views.leaderboard),
    (r'^mypage/$', views.my_page),
    (r'^mypage/(?P<opt>\d+)$', views.my_page),
    (r'^teamp/$', views.teamp),
    (r'^error/$', views.error)
)
