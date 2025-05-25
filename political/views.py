from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import QuestionForm
from .models import Question, Event


# Create your views here.
def landing(request):
    """
    This function renders the landing page.

    :param request: The HTTP request object.
    :return: Rendered landing page.
    :rtype: HttpResponse
    """
    return render(request, 'political/landing.html')


def signup(request):
    """
    This function renders the signup page and handles user registration.
    
    :param request: The HTTP request object.

    :return: Rendered signup page with the user creation form.

    :rtype: HttpResponse
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('political:login')
    else:
        form = UserCreationForm()
    return render(request, 'political/signup.html', {'form': form})


def authenticate_user(request):
    """
    This function authenticates the user based on the username and password

    :param request: The HTTP request object containing user credentials.

    :return: Redirects to the home page if authentication is successful,
             otherwise redirects to the login page with an error message.
    
    :rtype: HttpResponseRedirect
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not username or not password:
            # Handle missing username or password
            return render(request, 'registration/login.html', {
                'error_message': 'Username and password are required.'
            })

        user = authenticate(username=username, password=password)

        # If user is None, then the user is not authenticated. Redirect
        # the user to the login page.
        if user is None:
            return HttpResponseRedirect(reverse('political:login'))
        # If user is authenticated, then log the user in and redirect the
        # user to the political home page.
        else:
            login(request, user)
            return HttpResponseRedirect(reverse('political:home'))
    else:
        return HttpResponseRedirect(reverse('political:login'))


def user_login(request):
    """
    This function renders the login page.

    :param request: The HTTP request object.

    :return: Rendered login page.

    :rtype: HttpResponse
    """
    return render(request, 'registration/login.html')


def ask_question(request):
    """
    This function renders the home page where users can ask questions.

    :param request: The HTTP request object.

    :return: Rendered home page with the question form.

    :rtype: HttpResponse
    """
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('political:success')
    else:
        form = QuestionForm()
    return render(request, 'political/home.html', {'form': form})


def questions_list(request):
    """
    This function retrieves and displays all questions asked by users.

    :param request: The HTTP request object.

    :return: Rendered questions page with a list of all questions.

    :rtype: HttpResponse
    """
    questions = Question.objects.all()
    return render(request, 'political/questions.html', {'questions': questions})


def success(request):
    """
    This function renders the success page after a question is asked.

    :param request: The HTTP request object.

    :return: Rendered success page.

    :rtype: HttpResponse
    """
    return render(request, 'political/success.html')


def vision(request):
    """
    This function renders the vision and mission page.

    :param request: The HTTP request object.

    :return: Rendered vision and mission page.

    :rtype: HttpResponse
    """
    return render(request, 'political/vision_mission.html')


def campaign_dates(request):
    """
    This function retrieves and displays all campaign events.


    :param request: The HTTP request object.

    :return: Rendered campaign dates page with a list of all events.

    :rtype: HttpResponse
    """
    events = Event.objects.all()
    return render(request, 'political/campaign_dates.html', {'events': events})
