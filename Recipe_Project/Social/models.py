from django.db import models
from django.contrib.auth.models import User
from Recipe.models import Recipe


# This model represents the followers of users in your system
class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.follower.username} follows {self.user.username}"

# This model represents the likes given to recipes by users
class Like(models.Model):                   # =  FavoriteRecipe
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} liked {self.recipe.title}"

class FavoriteRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)




"""
The Follower model establishes a relationship between users, where one user follows another. This is a many-to-many relationship as one user can follow multiple users and be followed by multiple users.
The Like model represents a user's like on a recipe. It's linked to both the user and the recipe they liked.
Remember to create the appropriate foreign key relationships and use the related_name attribute to define the reverse relationship from the User model.
"""



"""
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)

    def __str__(self):
        return self.message
"""
"""
About Notification Model
user: A ForeignKey relationship to the User model, representing the user who will receive the notification.
message: The content of the notification message.
timestamp: The date and time when the notification was created.
seen: A boolean field indicating whether the user has seen the notification.
This Notification model allows you to store notifications for users and track whether they have been viewed. You can create notifications for various actions (e.g., comments, likes, follows) and display them to users when they log in.
"""