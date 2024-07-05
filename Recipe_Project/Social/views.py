from django.shortcuts import render,HttpResponse

# Create your views here.
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import Recipe, Like, FavoriteRecipe
from django.contrib import messages
from django.http import JsonResponse


@login_required
def add_likes_view(request, id):
    recipe = get_object_or_404(Recipe, pk=id)

    existing_like = Like.objects.filter(user=request.user, recipe=recipe).first()

    if existing_like:
        existing_like.delete()
    else:
        Like.objects.create(user=request.user, recipe=recipe)

    return redirect(f'/recipe-/recipe_detail/{recipe.id}', id=recipe.id)

@login_required
def likes_view(request,id):
    recipe = get_object_or_404(Recipe, id=id)
    likes_count = Like.objects.filter(recipe=recipe).count()
    return render(request,'recipe_list.html',{'likes_count':likes_count})


@login_required
def add_to_favorites(request, id):
    recipe = get_object_or_404(Recipe, pk=id)

    # Check if the recipe is already in the user favorites
    existing_favorite = FavoriteRecipe.objects.filter(user=request.user, recipe=recipe).first()

    if existing_favorite:
        # If the recipe is already in favorites, remove it
        existing_favorite.delete()
    else:
        # If the recipe is not in favorites, add it
        FavoriteRecipe.objects.create(user=request.user, recipe=recipe)
        messages.success(request,"Added Successfully")
        
    # JsonResponse({"status": "error"}, status=400)
    return redirect(f'/recipe-/recipe_detail/{recipe.id}', id=recipe.id)  # Redirect back to the recipe detail page

@login_required
def favorite_recipes(request):
    # Retrieve the favorite recipes for the current user
    favorite_recipes = FavoriteRecipe.objects.filter(user=request.user)
    return render(request, 'favorite.html', {'favorite_recipes': favorite_recipes})