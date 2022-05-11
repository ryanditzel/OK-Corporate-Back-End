from ok_corporate import serializers
from . import views
from django.urls import path
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    # JavaScript Web Tokens
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token-create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token-refresh'),
    path('blacklist/', views.UserLogout.as_view(),
         name='token-blacklist'),
    # User paths
    path('users/', views.UserList.as_view(), name='user_list'),
    path('users/create', views.UserCreate.as_view(), name='user_create'),
    path('users/logout', views.UserLogout.as_view(), name='user_logout'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('users/<str:username>', views.UserDetailByUsername.as_view(),
         name='user_detail_by_username'),
    # Review paths
    path('reviews/', views.ReviewList.as_view(), name='review_list'),
    path('reviews/<int:pk>', views.ReviewDetail.as_view(), name='review_detail'),
    # Company paths
    path('company/', views.CompanyList.as_view(), name='company_list'),
    path('company/<int:pk>', views.CompanyDetail.as_view(), name='company_detail'),

]
