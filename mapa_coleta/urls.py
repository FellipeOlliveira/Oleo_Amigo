from django.urls import path
from .views import UserListCreateView, UserDetailView , TesteApiDetailView ,TesteApiListCreateView , EnderecoListCreateView , EnderecoDetailView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create')
    ,path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail')
    ,path('teste_api/', TesteApiListCreateView.as_view(), name='teste_api_list_create')
    ,path('teste_api/<int:pk>/', TesteApiDetailView.as_view(), name='teste_api_detail')
    ,path('enderecos/', EnderecoListCreateView.as_view(), name='enderecos-list-create')
    ,path('enderecos/<int:pk>/', EnderecoDetailView.as_view(), name='enderecos-detail'),
]