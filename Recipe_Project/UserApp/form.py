from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserProfile
from django.forms.widgets import FileInput

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']
        
class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = UserProfile
        fields = ['profile_image', 'zipcode', 'birth_date']
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ProfileForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name

    def save(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        if user:
            user.first_name = self.cleaned_data['first_name']
            user.last_name = self.cleaned_data['last_name']
            user.save()
        return super(ProfileForm, self).save(*args, **kwargs)










# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django import forms
# from .models import UserProfile

# class SignUpForm(UserCreationForm):
#     class Meta:
#         model=User
#         fields='__all__'   #['first_name','last_name','email']
        
# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['profile_image','bio','location','birth_date','facebook']