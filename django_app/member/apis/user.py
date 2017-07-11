from rest_framework import permissions
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from utils.permissions import ObjectIsRequestUser
from ..models import User

from ..serializers import UserSerializer


class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        ObjectIsRequestUser,
    )


