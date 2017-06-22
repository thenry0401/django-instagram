from django.conf.urls import url

from . import views

app_name = 'member'
urlpatterns = [
    url(r'^login/$', views.login, name='login'),
<<<<<<< HEAD

    url(r'^logout/$', views.logout, name='logout'),

    url(r'^signup/$', views.signup, name='signup'),

    url(r'^profile/$', views.profile, name='myprofile'),
    url(r'^profile/(?P<user_pk>\d+)/$', views.profile, name='profile'),
]
=======
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    # profile view의 0번
    url(r'^profile/$', views.profile, name='my_profile'),
    url(r'^profile/(?P<user_pk>\d+)/$', views.profile, name='profile'),
]
>>>>>>> e5278c3fc0369ff8fa911dace01b1d0a28cb1c8d
