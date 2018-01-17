from django.urls import path
from accounts import views
from accounts.views import (CreateUserView, AdminProfileView, UserProfileView,
                            CreateEmployee,)
from django.contrib.auth.views import login, logout

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', login, {'template_name': 'accounts/login.html'}, name='login'),
    path('logout/', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('new-employee/', CreateEmployee.as_view(), name='add_employee'),
    path('my-profile', views.myProfile, name='my_profile'),
    path('<int:pk>/admin/home/', AdminProfileView.as_view(), name='admin_home'),
    path('<int:pk>/user/home/', UserProfileView.as_view(), name='user_profile'),
]
