from rest_framework.generics import ListAPIView
from .serializers import userserializer , found_items_serializer,found_items_user_serializer
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import found_items
from datetime import datetime
# Create your views here.

class create_User(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = userserializer
    permission_classes = [AllowAny]
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
         

class found_item_listCreate(generics.ListCreateAPIView):
    serializer_class=found_items_serializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        return found_items.objects.all()
    def perform_create(self, serializer):
       if serializer.is_valid():
            serializer.save(username=self.request.user)
       else:
            print(serializer.errors)

class found_item_user(ListAPIView):
    serializer_class=found_items_user_serializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        username=self.request.user
        return found_items.objects.filter(username=username)


class found_item_delete(generics.DestroyAPIView):
    serializer_class=found_items_user_serializer
    permission_classes=[IsAuthenticated]
    def get_queryset(self):
        username=self.request.user
        return found_items.objects.filter(username=username)