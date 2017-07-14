"""
member application생성
    settings.AUTH_USER_MODEL모델 구현
        username, nickname
이후 해당 settings.AUTH_USER_MODEL모델을 Post나 Comment에서 author나 user항목으로 참조
"""
import re

import time
from django.conf import settings
from django.db import models
from django.db.models.signals import post_delete
from django.db.models.signals import post_save
from django.dispatch import receiver

from utils.fields import CustomImageField

__all__ = (
    'Post',
    'PostLike',
)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    photo = CustomImageField(upload_to='post', blank=True)
    video = models.ForeignKey('Video', blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    my_comment = models.OneToOneField(
        'Comment',
        blank=True,
        null=True,
        related_name='+'
    )
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='like_posts',
        through='PostLike',
    )
    like_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-pk', ]

    def add_comment(self, user, content):
        # 자신을 post로 갖고, 전달받은 user를 author로 가지며
        # content를 content필드내용으로 넣는 Comment객체 생성
        return self.comment_set.create(author=user, content=content)

    def calc_like_count(self):
        self.like_count = self.like_users.count()
        self.save()

    @property
    def comment(self):
        if self.my_comment:
            return self.comment_set.exclude(pk=self.my_comment.pk)
        return self.comment_set.all()

class PostLike(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            ('post', 'user'),
        )


@receiver(post_save, sender=PostLike)
@receiver(post_delete, sender=PostLike)
def update_post_like_count(sender, instance, **kwargs):
    print('Signal update_post_like_count, instance: {}'.format(
        instance
    ))
    instance.post.calc_like_count()