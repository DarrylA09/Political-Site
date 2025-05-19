from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    """
    This class represents the Question form.
    """
    class Meta:
        model = Question
        fields = ['question_text']
        widgets = {
            'question_text': forms.Textarea(attrs={'placeholder': 'Type your question here...', 'class': 'form-control'}),
        }


class LoginForm(forms.Form):
    """
    This class represents the login form.
    """
    username = forms.CharField(
        max_length=100, 
        label="Your Username",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username', 'style': 'color: white;'})
    )
    password = forms.CharField(
        label="Your Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password', 'style': 'color: white;'})
    )
