"""
URL configuration for Recipe_Pro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

# from Recipe.views import *
from Recipe.views import recipe_list
from AdminApp.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('/',all_recipes),
    path('',recipe_list,name='HomePage'),
    # path('',recipe_list,name='recipe_list'),
    path('recipe-/',include(('Recipe.urls','Recipe'),namespace='RecipeAppUrls')),
    path('Userapp-/',include(('UserApp.urls','UserApp'),namespace='UserAppUrls')),
    path('Social-/',include(('Social.urls','Social'),namespace='SocialAppUrls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
