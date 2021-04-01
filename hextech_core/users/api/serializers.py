from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "avatar"]

    @staticmethod
    def get_avatar(user: User) -> str:
        return user.wagtail_userprofile.avatar.url
