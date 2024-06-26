from django import forms

from .models import *


from django import forms
from django.contrib.auth.forms import UserCreationForm




class AccountCreationForm(UserCreationForm):
	email = forms.EmailField(max_length=254, help_text='Required. Add a valid email address.')

	class Meta:
		model = Account
		exclude = ['is_active','date_joined', 'last_login', 'is_admin','is_staff', 'is_superuser', 'id', 'applied']

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(email=email)
		except Account.DoesNotExist:
			return email
		raise forms.ValidationError('Email "%s" is already in use.' % account)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			account = Account.objects.exclude(pk=self.instance.pk).get(username=username)
		except Account.DoesNotExist:
			return username
		raise forms.ValidationError('Username "%s" is already in use.' % username)
