from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('', views.api_root),
    path('wishlist/',views.WishListList.as_view(), name = 'wish-list, create'),
    path('wishlist/<int:pk>/', views.WishListDetail.as_view()),
    path('user/', views.UserList.as_view(), name = 'user-list'),
    path('user/create/', views.UserCreate.as_view(), name= 'user-create'),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('product/', views.ProductList.as_view(), name = 'product-list'),
    path('product/create/', views.ProductCreate.as_view(), name = 'create'),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)