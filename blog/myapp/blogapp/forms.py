from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import password_validators_help_texts
from .models import Post

class LoginForm(forms.Form):
    username = forms.CharField(
        label = 'Username',
        max_length = 150,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}))
    password = forms.CharField(
                               label = 'Password,',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}))
    
    
class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required = True,
        label= 'Email',
        widget = forms.EmailInput(attrs={'class':'form-control'}))
    
    username = forms.CharField(
        required=True,
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.')

    password1 = forms.CharField(
        required = True,
        label= 'Password',
        widget = forms.TextInput(attrs = {'class':'form-control'}),
        help_text='<ul>' + ''.join([f'<li>{text}</li>' for text in password_validators_help_texts()]) + '</ul>')
    password2 = forms.CharField(
        required = True,
        label= 'Confirm password',
        widget = forms.TextInput(attrs = {'class':'form-control'}),
        help_text = 'You must enter same password you entered above.'
        )
    
        
    class Meta:
        model = User 
        fields = ['username','email','password1','password2']

    
class PostForm(forms.ModelForm):
     class Meta:
         model = Post 
         fields = ['title','description']
         widgets = {
             'title': forms.TextInput(attrs = {'class':'form-control'}),
             'description':forms.Textarea(attrs = {'class':'form-control'})
         }
        
        
