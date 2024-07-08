from django.shortcuts import render, redirect
from Recipe.models import Recipe
from .form import SignUpForm, ProfileForm
from .models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
import random
from django.core.mail import send_mail
from Recipe_Pro.settings import EMAIL_HOST_USER

@unauthenticated_user
def register_user(request):
    form = SignUpForm()
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            otp = random.randint(100000, 999999)
            request.session['otp'] = otp
            send_mail(
                'Otp Verification From Recipe App',
                f'Your OTP code for SignUp is {otp}',
                EMAIL_HOST_USER,
                [user.email],
                fail_silently=False,
            )
            messages.success(request,'Register Succcessfully Please Verify Otp..')
            return redirect('/Userapp-/verify_otp/')
        else:
            messages.error(request,'Invalid Credentials..')
            return render(request,'signup.html',{'form':form})
    return render(request,'signup.html',{'form':form})

@unauthenticated_user
def verify_otp(request):
    if request.method == 'POST':
        otp = (request.POST.get('otp'))
        session_otp = request.session.get('otp')
        if otp == str(session_otp):
            try:
                messages.success(request, 'Your account has been verified.')
                del request.session['otp']
                return redirect('/Userapp-/login/')
            except Exception as e:
                messages.error(request, f'User not found : {e}')
        else:
            messages.error(request, 'Invalid OTP.')
    return render(request, 'verify_otp.html')

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

# @login_required(login_url='UserApp:login_form')
# def logout_user(request):
#     logout(request)
#     messages.info(request,'Logged out successfully..')
#     return redirect('/')

def user_recipes(request):
    r = Recipe.objects.filter(author=request.user)
    return render(request,'my_recipes.html',{'myrecipes':r})

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