from django.conf.urls import url

from post import apis

urlpatterns = [
    url(r'^$', apis.PostListCreateView.as_view()),
]