from django.urls import path
from .import views

app_name = "political"

# URL patterns for the political app
urlpatterns = [
    path('', views.landing, name='landing'),
    path('accounts/login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path(
        'accounts/authenticate/',
        views.authenticate_user,
        name='authenticate_user'
    ),
    path('home/', views.ask_question, name='home'),
    path('questions/', views.questions_list, name='questions_list'),
    path('success/', views.success, name='success'),
    path('vision/', views.vision, name='vision'),
    path('campaign-dates/', views.campaign_dates, name='campaign_dates')
]
