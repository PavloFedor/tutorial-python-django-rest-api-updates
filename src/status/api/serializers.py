from rest_framework import serializers

from status.models import Status
from accounts.api.user.serializers import UserDetailSerializer


class StatusSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image'
        ]
        read_only_fields = ['user']

    def validate_content(self, value):
        if len(value) > 1000000:
            raise serializers.ValidationError("This is wayy too long")
        return value

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("Status should have content or image")
        return data
