from django.forms.models import model_to_dict
from .models import Category
from .serializers import CategorySerializer

def create_category(data):
    serializer = CategorySerializer(data=data)
    if serializer.is_valid():
        category = serializer.save()
        return category
    return None

def get_category_tree(category):
    category_dict = model_to_dict(category, fields=['category_name', 'status', 'id'])
    parent = category.parent

    if parent:
        category_dict['parent'] = get_category_tree(parent)

    children = category.children.all()
    if children.exists():
        category_dict['children'] = [get_category_tree(child) for child in children]

    return category_dict