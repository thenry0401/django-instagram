from django.conf.urls import url

from . import views

urlpatterns = [
    # /post/$
    url(r'^$', views.post_list),

    # /post/숫자, 위치인수로 반환하는 방법
    # url(r'^(\d+)/$', views.post_detail),

    # 키워드인수로 반환하는 방법
    url(r'^(?P<post_pk>\d+)/$', views.post_detail),
]