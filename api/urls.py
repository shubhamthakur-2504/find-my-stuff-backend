from django.urls import path
from api import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
urlpatterns = [
    path('user/register/',views.create_User.as_view(), name='register'),
    path('token/',TokenObtainPairView.as_view(),name='get_token'),
    path('token/refresh/', TokenRefreshView.as_view(),name='refresh_token'),
    path('found-item/',views.found_item_listCreate.as_view(),name='found-items'),
    path('found-item/user',views.found_item_user.as_view(),name='found-items-user'),
    path('found-item/delete/<int:pk>/',views.found_item_delete.as_view(),name='delete item')
]
