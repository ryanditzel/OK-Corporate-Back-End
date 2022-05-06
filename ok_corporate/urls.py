from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('reviews/', views.ReviewList.as_view(), name='review_list'),
    path('reviews/<int:pk>', views.ReviewDetail.as_view(), name='review_detail'),
    path('company/', views.CompanyList.as_view(), name='company_list'),
    path('company/<int:pk>', views.CompanyDetail.as_view(), name='company_detail'),
    path('user/', views.CompanyList.as_view(), name='company_list'),
    path('user/<int:pk>', views.CompanyDetail.as_view(), name='company_detail'),
]
