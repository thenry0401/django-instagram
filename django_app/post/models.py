"""
member application 생성
    User모델 구현,
        username, nickname
이후 해당 User모델 Post나 Comment에서 author나 user 항목으로 참조
"""

from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(User)
    photo = models.ImageField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(
        User,
        related_name='like_posts',
        through='PostLike'
    )
    tags = models.ManyToManyField('Tag')

    def add_comment(self, user, content):
        return self.comment_set.create(
            author=user,
            content=content
        )

    def add_tag(self, tag_name):
        tag, tag_created = Tag.objects.get_or_create(name=tag_name)
        if not self.tags.filter(name=tag_name).exist():
            self.tags.add(tag)

    @property
    def like_count(self):
        return self.like_users.count()


class PostLike(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(User)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(
        User,
        through='CommentLike',
        related_name='like_comments',
    )

class CommentLike(models.Model):
    comment = models.ForeignKey(Comment)
    user = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return 'Tag({})'.format(self.name)
