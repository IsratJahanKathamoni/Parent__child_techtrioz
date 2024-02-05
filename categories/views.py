
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Category
from .serializers import CategorySerializer
from .utils import get_category_tree


@api_view(['GET', 'POST'])
def category_tree_api(request):
    if request.method == 'GET':
        # Handle GET request
        root_categories = Category.objects.filter(parent__isnull=True)
        serialized_tree = [get_category_tree(category) for category in root_categories]
        return Response(serialized_tree)

    elif request.method == 'POST':
        # Handle POST request
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    