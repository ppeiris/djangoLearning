from django import forms
from frontend.models import Profile, User, UserProfile


class ProfileForm(forms.ModelForm):
	name = forms.CharField(max_length = 128, help_text = "Please enter the Profile name")

	class Meta:
		model = Profile
		fields = ('name', )


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('picture',)

