"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
<<<<<<< HEAD
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from django.conf import settings
=======
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView
>>>>>>> e5278c3fc0369ff8fa911dace01b1d0a28cb1c8d

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

<<<<<<< HEAD
    # 기본 주소를 /post/로 리다이렉트 시키기
    url(r'^$', views.index, name='index'),
    # url(r'^$', RedirectView.as_view(pattern_name'post:post_list))
    # 두번째는 view를 만들지않고 바로 쓸 수 있는 커맨드이다

    url(r'^post/', include('post.urls')),

    url(r'^member/', include('member.urls')),
] + static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
   )
=======
    # post앱의 index뷰를 root url에 연결시킨다.
    # url(r'^$', post_views.index),

    # 새 view를 만들어 redirect시키는 방법
    url(r'^$', views.index, name='index'),

    # Class-based View중 RedirectView를 사용하는 방법
    # url(r'^$', RedirectView.as_view(pattern_name='post:post_list')),

    # post앱의 urls.py모듈을 include시킨다
    url(r'^post/', include('post.urls')),
    url(r'^member/', include('member.urls')),
]
urlpatterns += static(
    prefix=settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
>>>>>>> e5278c3fc0369ff8fa911dace01b1d0a28cb1c8d
