from rest_framework import serializers
from django.contrib.auth.models import User
from .models import found_items

class userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']
        extra_kwargs={'password':{'write_only':True}}

    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        return user

class found_items_serializer(serializers.ModelSerializer):
    class Meta:
        model=found_items
        fields=[ 'name','address','phone_no','keywords','description','img','username','date_created' ]
        extra_kwargs={'username':{'read_only': True}}

class found_items_user_serializer(serializers.ModelSerializer):
    username = serializers.CharField(source='username.username', read_only=True)
    class Meta:
        model=found_items
        fields=['username','id' ,'name','img']
