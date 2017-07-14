from rest_framework import serializers

from member.serializers import UserSerializer
from post.serializers.comment import CommentSerializer
from ..models import Post

__all__ = (
    'PostSerializer',
)


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    my_comment = CommentSerializer(read_only=True)
    comments = CommentSerializer(read_only=True, many=True, source='comment_set')
    class Meta:
        model = Post
        fields = (
            'pk',
            'author',
            'photo',
            'my_comment',
            'comments',
        )
        read_only_fields = (
            'author',
            'my_comment',
        )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['is_like'] = self.context['request'].user in instance.like_users.all()