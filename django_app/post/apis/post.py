from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Post
from post.serializers.post import PostSerializer

__all__ = (
    'PostListView',
)

class PostListView(APIView):
    # get 요청이 왔을 때, Post.objects.all()을 PostSerializer를 통해 Response로 반환
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)