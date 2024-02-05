from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.SerializerMethodField()
    children = serializers.SerializerMethodField()

    def get_parent(self, obj):
        parent_obj = obj.parent
        if parent_obj:
            return CategorySerializer(parent_obj).data
        return None

    def get_children(self, obj):
        children_queryset = obj.children.all()
        children_serializer = CategorySerializer(children_queryset, many=True)
        return children_serializer.data

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'status', 'parent', 'children']