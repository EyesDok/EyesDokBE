from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        # Get the value of senior_member from the form data
        membership = request.POST.get('membership') == 'true'

        # Create the user in the database
        user = CustomUser.objects.create_user(username=username, email=email, password=password1, membership=membership)
        user.save()

        # Redirect to a success page after successful registration
        return redirect('accounts:signup')
    return render(request, 'accounts/signup.html')
