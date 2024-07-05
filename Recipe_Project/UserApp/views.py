from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from Recipe.models import Recipe
from .form import ProfileForm                                       # Edit Profile Karne Ke Liye
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout           #,user_logged_in,user_logged_out
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user

# @unauthenticated_user
# def register_user(request):
#     if request.method=='POST':
#         f=UserCreationForm(request.POST)
#         if f.is_valid():                                            
#             messages.success(request,'Account Created Successfully')
#             f.save()
#             return redirect('/Userapp-/login/')
#     else:
#         f=UserCreationForm()
#         return render(request,'signup.html',{'register':f})

@unauthenticated_user
def register_user(request):
    form = UserCreationForm()
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request,'Register Succcessfully..')
            return redirect('/Userapp-/login/')
        else:
            messages.info(request,'Invalid Credentials..')
            return render(request,'signup.html',{'form':form})
    return render(request,'signup.html',{'form':form})

@unauthenticated_user
def login_user(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username=username ,password=password)
        if user is not None:
            login(request,user)
            messages.info(request, f'{username} Your Logged in ..')
            return redirect('/')
        else:
            messages.info(request,'Invalid Username or password ...!!!')
            
    return render(request,'login.html')

# def login_user(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, 'You have successfully logged in!')
#                 return redirect('/')  # Change 'home' to your desired redirect URL
#             else:
#                 messages.info(request, 'Invalid username or password.')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.info(request,'Logged out successfully..')
    return redirect('/')

def user_recipes(request):
    r = Recipe.objects.filter(author=request.user)
    return render(request,'my_recipes.html',{'myrecipes':r})

# @login_required(login_url='UserApp:login_form')
# def user_profile(request):
#     return render(request,'user_profile.html')


@login_required(login_url='UserApp:login_form')
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile, user=request.user)
        if form.is_valid():
            form.save(user=request.user)
            messages.success(request, " Your Profile is updated..")
            return redirect('/Userapp-/profile/')  # Assuming you have a profile view to redirect to after saving
    else:
        # messages.success(request, "Fill The Form Correctly..")
        form = ProfileForm(instance=user_profile, user=request.user)

    return render(request, 'profile.html', {'form': form})

# @login_required(login_url='UserApp:login_form')
# def edit_profile(request):
#     if request.method=='POST':
#         form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
#         if form.is_valid():
#             form.save()
#             username = request.user
#             messages.success(request, " Your Profile is updated..")
#             return redirect('/')
#     else:
#         form = ProfileForm(instance=request.user.userprofile)
#     return render(request,'edit_profile.html',{'form':form})