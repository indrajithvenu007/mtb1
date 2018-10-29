from django import forms
from .models import Comment

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Customer

class UserForm(UserCreationForm):
     class Meta:
         model = User
         fields = ['username','first_name','last_name','email','password1','password2']

class CustomerForm(forms.ModelForm):
     class Meta:
         model = Customer
         exclude = ('user_data',)

class CommentForm(forms.ModelForm):
	text = forms.CharField(
		widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
		required=True,
		max_length=1000
		)

	class Meta:
		model = Comment
		fields = ('text', )