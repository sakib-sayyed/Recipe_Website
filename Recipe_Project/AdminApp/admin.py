from django.contrib import admin
from Recipe.models import Recipe,Comment
from UserApp.models import UserProfile
from Social.models import Follower ,Like
# Register your models here.

admin.site.register(Recipe)
admin.site.register(Comment)

admin.site.register(UserProfile)

admin.site.register(Follower)
admin.site.register(Like)