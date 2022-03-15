from urllib import response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer, serializers
from .models import Product
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def products_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)