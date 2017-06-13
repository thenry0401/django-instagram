

from django.conf import settings
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template import loader

from .models import Post, Comment


def post_list(request):
    # 모든 Post목록을 'posts'라는 key로 context에 담아 return render처리
    # post/post_list.html을 template으로 사용하도록 한다

    # 각 포스트에 대해 최대 4개까지의 댓글을 보여주도록 템플릿에 설정
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'post/post_list.html', context)


def post_detail(request, post_pk):
    try:
        post = Post.objects.get(pk=post_pk)
    except Post.DoexNotExist as e:
        # return HttpResponseNotFound('Post not found, detail : {}.'.format(e))

        return redirect('post:post_list')

    template = loader.get_template('post/post_detail.html')
    context = {
        'post' : post
    }
    rendered_string = template.render(context=context, request=request)
    return HttpResponse(rendered_string)

def post_create(request):
    # POST요청을 받아 Post객체를 생성 후 post_list페이지로 redirect
    if request.method == 'POST':
        data = request.POST
        user = settings.AUTH_USER_MODEL.objects.first()
        content = data['text']
        post = Post.objects.create(
            author=user,
            content=content,
        )
        return redirect('post/post_list.html', pk=post.pk)


def post_modify(request, post_pk):
    # 수정
    pass


def post_delete(request, post_pk):
    # post_pk에 해당하는 Post에 대한 delete요청만을 받음
    # 처리완료후에는 post_list페이지로 redirect
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post/post_list.html')

def comment_create(request, post_pk):
    # POST요청을 받아 Comment객체를 생성 후 post_detail페이지로 redirect
    if request.method == 'POST':
        data = request.POST
        user = settings.AUTH_USER_MODEL.objects.first()
        content = data['text']
        post = Comment.objects.create(
            author=user,
            content=content,
        )
        return redirect('post/post_list.html', pk=post_pk)


def comment_modify(request, post_pk):
    # 수정
    pass


def comment_delete(request, post_pk, comment_pk):
    # POST요청을 받아 Comment객체를 delete, 이후 post_detail페이지로 redirect
    post = Comment.objects.get(pk=post_pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post/post_list.html')