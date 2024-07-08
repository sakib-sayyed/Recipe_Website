from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('signup/', register_user, name='signup_form'),
    path('verify_otp/',verify_otp,name='verify_otp'),
    path('login/', login_user, name='login_form'),
    # path('logout/', logout, name='logout_form'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout_form'),
    path('user_recipes/', user_recipes, name='user_recipes'),
    path('profile/', profile, name='profile'),
]
