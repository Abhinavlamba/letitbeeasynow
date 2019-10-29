from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from letitbeeasy import views
from django.conf.urls import include

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('content/', views.ContentList.as_view()),
    path('content/<int:pk>/', views.ContentDetail.as_view()),
]
urlpatterns += [
    path('', views.api_root),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)