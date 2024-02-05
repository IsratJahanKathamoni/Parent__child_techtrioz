


from django.urls import path
from .views import category_tree_api

urlpatterns = [
    path('category-tree/', category_tree_api, name='category_tree_api'),
    # Add other URLs specific to the 'categories' app as needed
    
    
]
