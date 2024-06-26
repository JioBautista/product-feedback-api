from api.models import ProductRequests
from api.serializers import ProductRequestsSerializers
from rest_framework import viewsets


class ProductRequestsViewSet(viewsets.ModelViewSet):
    queryset = ProductRequests.objects.all()
    serializer_class = ProductRequestsSerializers
