from django import forms
from django.forms import inlineformset_factory
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'cooking_time', 'servings', 'description', 'image' , 'description', 'ingredients','instructions','category' ]
        # widgets = {
        #     'ingredients': forms.Textarea(attrs={'rows': 4}),  # You can adjust the number of rows as needed
        # }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'ingredients': forms.Textarea(attrs={'rows': 5}),
            'instructions': forms.Textarea(attrs={'rows': 5}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }