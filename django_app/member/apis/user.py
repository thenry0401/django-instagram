from rest_framework import permissions
from rest_framework import status, generics

from member.serializers.user import UserCreationSerializer
from utils.permissions import ObjectIsRequestUser
from ..models import User

from ..serializers import UserSerializer

__all__ = (
    'UserRetrieveUpdateDestroyView',
    'UserListCreateView'
)


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializer
        elif self.request.method == 'POST':
            return UserCreationSerializer


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        ObjectIsRequestUser,
    )




