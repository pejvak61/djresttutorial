"""
useraccounts.Urls.py
"""
from django.urls import path
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from useraccounts import views


urlpatterns = [
    path('listallusers/', views.SnippetList.as_view(), name='snippets_Ali'),
    path('addnewuser/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns += format_suffix_patterns(urlpatterns)
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
