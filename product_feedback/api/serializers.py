from rest_framework import serializers
from api.models import CurrentUser, ProductRequests


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentUser
        fields = "__all__"
