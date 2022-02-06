from .models import WishList, Product
from django.contrib.auth.models import User
from .serializers import WishListSerializer, UserSerializer, ProductSerializer
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.db.models import Count


class WishListList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = WishListSerializer
    
    def perform_create(self, serializer): 
        serializer.save(owner=self.request.user)
        

    def get_queryset(self):
        #This row checks if the user is superuser for show all the wishlists
        if self.request.user.is_staff == True:
            return WishList.objects.all()
        else:
            return WishList.objects.filter(owner=self.request.user)
    
   
class WishListDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    
    
class ProductCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductList(generics.ListAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Product.objects.annotate(
        number_of_wishes = Count('wishlist__owner_id', distinct=True)
    )
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class UserCreate(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer
          
     
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

@api_view(['GET'])
@permission_classes((AllowAny,))
def api_root(request, format=None):
    return Response({
        'create user': reverse('user-create', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'wishlists': reverse('wish-list, create', request=request, format=format),
        'create product': reverse('create', request=request, format=format),
        'products list': reverse('product-list', request=request, format=format),
        
    })

