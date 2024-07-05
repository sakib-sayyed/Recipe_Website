from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='media/profile_images/profile-png-man.webp',upload_to='media/profile_images/', blank=True, null=True)
    zipcode = models.IntegerField(blank=True,null=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"



# More Fields
    # bio = models.TextField(max_length=500 , blank=True)
    # location = models.CharField(max_length=200, null=True)
    # facebook = models.URLField(max_length=200, null=True,blank=True)
    # twitter = models.URLField(max_length=200, blank=True)
    # instagram = models.URLField(max_length=200, blank=True)
    # website = models.URLField(max_length=200, blank=True)
    
    
    
# In this example:
"""
user: One-to-one relationship with the built-in User model provided by Django's authentication system.
profile_image: An image field to store the user's profile picture.
bio: A text field for the user's bio or description.
location: A field for the user's location.
website, facebook, twitter, instagram: Fields for links to the user's website and social media profiles.
This UserProfile model extends the default User model provided by Django, adding custom fields for the user's profile information.
"""