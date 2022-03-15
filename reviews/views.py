from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Review
from .serializers import ReviewSerializer, serializers

# Create your views here.

@api_view(['GET'])
def review_list(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)