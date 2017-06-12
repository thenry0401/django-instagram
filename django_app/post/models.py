"""
member application 생성
    User모델 구현,
        username, nickname
이후 해당 User모델 Post나 Comment에서 author나 user 항목으로 참조
"""

from django.contrib.auth.models import User
from django.db import models


# class User(models.Model):
#     name = models.CharField(max_length=30)


class Post(models.Model):
    author = models.ForeignKey(User)
    photo = models.ImageField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(
        User,
        related_name='like_posts'
    )
    tags = models.ManyToManyField('Tag')


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(User)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Tag({})'.format(self.name)
