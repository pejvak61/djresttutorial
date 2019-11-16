"""
useraccounts.Urls.py
"""
from django.urls import path
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns
from useraccounts import views


urlpatterns = [
    path('listallusers/', views.ListAllUsers.as_view()),
    path('addnewuser/', views.CreateNewUser.as_view()),
    path('listalluserdetails/', views.ListAllUserDetails.as_view()),
    path('addnewuserdetail/', views.CreateNewUserDetail.as_view()),
    path('listalluserpasswords/', views.ListAllUserPasswords.as_view()),
    path('addnewuserpassword/', views.CreateNewUserPassword.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

urlpatterns += format_suffix_patterns(urlpatterns)
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
