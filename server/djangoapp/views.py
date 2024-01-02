# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def about(request):
    # Add logic for the about page if necessary
    return render(request, 'djangoapp/about.html')

def contact(request):
    # Add logic for the contact page if necessary
    return render(request, 'djangoapp/contact.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('djangoapp:home')
        else:
            # Handle invalid login
            pass

    return render(request, 'djangoapp/login.html')

def logout_view(request):
    logout(request)
    return redirect('djangoapp:home')

def registration_request(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('djangoapp:home')
    else:
        form = UserCreationForm()

    return render(request, 'djangoapp/registration.html', {'form': form})

@login_required
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)

def get_dealer_details(request, dealer_id):
    # Add logic for getting dealer details if necessary
    return render(request, 'djangoapp/dealer_details.html', {'dealer_id': dealer_id})

def add_review(request, dealer_id):
    # Add logic for adding a review if necessary
    return render(request, 'djangoapp/add_review.html', {'dealer_id': dealer_id})

@login_required
def home(request):
    # Add logic for the home page if necessary
    return render(request, 'djangoapp/index.html', {})

# Add the signup view
def signup_view(request):
    if request.method == 'POST':
        # Process signup form data and create a new user
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
        login(request, user)
        return redirect('djangoapp:home')

    return render(request, 'djangoapp/registration.html')
