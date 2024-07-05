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
from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static

from Social.views import add_likes_view, add_to_favorites, likes_view, favorite_recipes

urlpatterns = [
    path('add_likes_view/<int:id>/', add_likes_view, name='add_likes_view'),
    path('like/<int:id>/',likes_view,name='like'),
    path('add_to_favorites/<int:id>/', add_to_favorites, name='add_to_favorites'),
    path('favorite_recipes/', favorite_recipes, name='favorite_recipes'),

]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
