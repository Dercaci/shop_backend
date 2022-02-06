from .models import WishList, Product
from django.contrib.auth.models import User
from rest_framework import serializers

from django.db.models import Count

class UserSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'wishlist']
        write_only_fields = ('password',)
        read_only_fields = ('id', 'wishlist')

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class WishListSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = WishList
        fields = ['id', 'owner', 'name', 'product']


class ProductSerializer(serializers.ModelSerializer):    
    number_of_wishes = serializers.IntegerField(read_only=True, default = 0)
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'number_of_wishes'] 
        


           



        




    
        
    
        
    

