from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label="Contrasena", widget=forms.PasswordInput)
	password2 = forms.CharField(label="Confirma tu contrasena", widget=forms.PasswordInput)

	class Meta():
		model = User
		fields = ('username', 'first_name', 'email')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Las contraseñas no coinciden')
		return cd['password2']

class UserEditForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name')

class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ( 'bio','date_of_birth', 'foto', 'avatar')
		widgets={
			'bio': forms.Textarea(attrs={'class':'materialize-textarea'})
		}