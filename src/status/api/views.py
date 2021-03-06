import rest_framework.mixins as mixins
import rest_framework.generics as generics
from rest_framework import permissions as permissions
import json
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication

from accounts.api.permissions import IsOwnerReadOnly
from status.models import Status
from .serializers import StatusSerializer


def is_json(json_data):
    try:
        json.loads(json_data)
        is_valid = True
    except ValueError:
        is_valid = False

    return is_valid


class StatusAPIDetailView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.RetrieveAPIView
):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerReadOnly]
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        print(request.data)
        return self.update(request, args, kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, args, kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, args, kwargs)


class StatusAPIView(
    mixins.CreateModelMixin,
    generics.ListAPIView
):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = StatusSerializer
    object_id = None,
    search_fields = ('user__username', 'content')
    ordering_fields = ('user_username', 'timestamp')
    queryset = Status.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
