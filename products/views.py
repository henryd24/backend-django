from .producer import publishmqtt
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, User
from .serializers import ProductSerializer

import random,json

class ProductViewSet(viewsets.ViewSet):
    def list(self, request): #/api/products
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    
    def create(self, request): # /api/products
        serializer = ProductSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publishmqtt('product_created', json.dumps(serializer.data))
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None): #/api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def update(self, request, pk=None): #/api/products/<str:id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publishmqtt('product_updated', json.dumps(serializer.data))
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None): #/api/products/<str:id>
        product = Product.objects.get(id=pk)
        product.delete()
        publishmqtt('product_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })