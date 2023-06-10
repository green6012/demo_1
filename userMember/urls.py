
from django.urls import path, include

from userMember import views
app_name = 'userMember'
urlpatterns = [

    # path('register/',views.registerUser.as_view(), name='registerUser'),
    path('register/',views.register, name = 'registerUser'),
    # path('login/', views.loginUser.as_view(), name='loginUser'),
    path('login/', views.loginPage, name='loginUser'),
    path('logout/',views.logoutUser, name='logout'),
    # path('private/',views.privateWeb, name='private')

]