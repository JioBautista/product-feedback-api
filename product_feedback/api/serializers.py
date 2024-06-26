from rest_framework import serializers
from api.models import CurrentUser, ProductRequests


class ProductRequestsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductRequests
        fields = "__all__"
