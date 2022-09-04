from django.urls import path
from .views import UserView, CategoriaView

urlpatterns = [
    path('users/', UserView.as_view(), name='user_list'),
    path('users/<int:_id>', UserView.as_view(), name='user_process'),
    path('categories/<int:_id>', CategoriaView.as_view(), name='categoria_process'),
    path('categories/', CategoriaView.as_view(), name='categoria_list')
]
