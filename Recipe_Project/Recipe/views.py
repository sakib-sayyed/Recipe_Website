from django.shortcuts import render, redirect ,get_object_or_404
from .models import Recipe
from .form import RecipeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Social.models import Like,FavoriteRecipe

@login_required
def add_recipe(request):
    if request.method=='POST':
        recipe_form = RecipeForm(request.POST,request.FILES)

        if recipe_form.is_valid():
            # Save the recipe
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('/')  # Redirect to a success page or recipe list
    else:
        recipe_form = RecipeForm()
        return render(request, 'add_recipe.html', {'recipe_form': recipe_form })


# def recipe_list(request):
#     recipes=Recipe.objects.all()
#     if request.method=='GET':
#         r_name = request.GET.get('recipename')
#         if r_name!=None:
#             recipes = Recipe.objects.filter(title__icontains=r_name)
#     return render(request,'recipe_list.html',{'all_recipe':recipes})

def recipe_list(request):
    recipes=Recipe.objects.all()
    likes_count = {}
    for recipe in recipes:
        likes_count[recipe.id] = Like.objects.filter(recipe=recipe).count()
    if request.method=='GET':
        r_name = request.GET.get('recipename')
        if r_name!=None:
            recipes = Recipe.objects.filter(title__icontains=r_name)
    return render(request,'home.html',{'all_recipe':recipes,'likes_count':likes_count,'query':r_name})

def recipe_detail(request,id): 
    recipe = get_object_or_404(Recipe, id=id)
    like_count = Like.objects.filter(recipe=recipe).count()
    favorite_count = FavoriteRecipe.objects.filter(recipe=recipe).count()
    
    # existing_favorite = FavoriteRecipe.objects.filter(user=request.user, recipe=recipe).first()
    # already_liked = Like.objects.filter(user=request.user, recipe=recipe).first()


    return render(request,'recipe_details.html',{'recipe':recipe,'likes_count':like_count,'favorite_count':favorite_count})

def edit_recipe(request,id):
    r=Recipe.objects.get(id=id)
    if request.method=='POST':
        f=RecipeForm(request.POST,request.FILES,instance=r)
        f.save()
        return redirect('/Userapp-/user_recipes/')
    else:
        recipe_form = RecipeForm(instance=r)

        return render(request, 'add_recipe.html', {'recipe_form': recipe_form})
        
def delete_recipe(request,id):
    r=Recipe.objects.get(id=id)
    r.delete()
    return redirect('/Userapp-/user_recipes/')