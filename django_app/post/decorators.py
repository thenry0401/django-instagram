from django.core.exceptions import PermissionDenied

<<<<<<< HEAD
from post.models import Post, Comment
=======
from .models import Post, Comment
>>>>>>> e5278c3fc0369ff8fa911dace01b1d0a28cb1c8d


def post_owner(f):
    def wrap(request, *args, **kwargs):
        post = Post.objects.get(pk=kwargs['post_pk'])
        if request.user == post.author:
            return f(request, *args, **kwargs)
        raise PermissionDenied

    return wrap

<<<<<<< HEAD
=======

>>>>>>> e5278c3fc0369ff8fa911dace01b1d0a28cb1c8d
def comment_owner(f):
    def wrap(request, *args, **kwargs):
        comment = Comment.objects.get(pk=kwargs['comment_pk'])
        if request.user == comment.author:
            return f(request, *args, **kwargs)
        raise PermissionDenied

<<<<<<< HEAD
    return wrap
=======
    return wrap
>>>>>>> e5278c3fc0369ff8fa911dace01b1d0a28cb1c8d
