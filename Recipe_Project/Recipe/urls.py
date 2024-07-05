from django.urls import path
from .views import add_recipe,recipe_detail,edit_recipe,delete_recipe
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('add_recipe/',add_recipe,name='add_recipe'),
    # path('recipe_list/',recipe_list,name='recipe_list'),
    path('recipe_detail/<int:id>/',recipe_detail,name='recipe_detail'),
    path('edit_recipe/<int:id>/',edit_recipe,name='edit_recipe'),
    path('delete_recipe/<int:id>/',delete_recipe,name='delete_recipe')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)