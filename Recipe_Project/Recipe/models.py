from django.db import models
from django.contrib.auth.models import User

# class Category(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

CATEGORY_CHOICES =(
    ('BreakFast','BreakFast'),
    ('Lunch','Lunch'),
    ('Dinner','Dinner'),
    ('Salad','Salad'),
    ('Cold-Drinks','Cold-Drinks'),
    ('Easy','Easy'),
    )


# This model represents the main recipe entity in our application.
class Recipe(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)       #Dont_Need_to_Take_Input
    updated_date = models.DateTimeField(auto_now=True)       #Dont_Need_to_Take_Input
    cooking_time = models.PositiveIntegerField()
    # prep_time = models.PositiveIntegerField()
    servings = models.CharField(max_length=50)
    description = models.TextField(max_length=1000)
    ingredients = models.TextField(max_length=2000)
    instructions = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='recipes/', blank=True , default="Unknown.jpg") # (upload_to='recipes/', blank=True, null=True)
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=50 , null=True , blank=True)
    
    class Meta:
        db_table = 'Recipe'

    def __str__(self):
        return self.title


# This model allows users to leave comments on recipes.
class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.recipe.title}"


# This model allows users to rate recipes.
class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating_value = models.PositiveIntegerField()

    def __str__(self):
        return f"Rating {self.rating_value} by {self.user.username} on {self.recipe.title}"





"""
The Recipe model stores information about a recipe, including its title, author, cooking time, preparation time, servings, difficulty level, and an optional image.
The Ingredient model represents each ingredient in a recipe, associated with a specific recipe.
The Instruction model stores each step of the recipe's instructions, linked to the corresponding recipe.
The Comment model allows users to leave comments on recipes, linked to both the recipe and the user.
The Rating model enables users to rate recipes with a numerical value, linked to the recipe and the user.
"""