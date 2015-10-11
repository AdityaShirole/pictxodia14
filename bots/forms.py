from django.forms import ModelForm, TextInput, Textarea, PasswordInput
from bots.models import Bot, Author

class SignUp(ModelForm):
	class Meta:
		model = Author
		exclude = ['attempts']
		labels = {
			'Name': 'Author Name',
			'Contact': 'Contact Number',
			'Email': 'Email id',
			'About': 'About you',
			'password': 'password',
			'username': 'username',
		}
		widgets = {
			'Name': TextInput(attrs = {'placeholder': 'Your Name*'}),
			'Contact': TextInput(attrs = {'placeholder': 'Contact no.*'}),
			'Email': TextInput(attrs= {'placeholder': 'Email id*'}),
			'About': Textarea(attrs = {'cols': 50, 'rows': 7, 'placeholder': 'Something about you'}),
			'password': PasswordInput(attrs = {'placeholder': 'password**',}),
			'username': TextInput(attrs = {'placeholder': 'unique username**'})
		}

class Login(ModelForm):
	class Meta:
		model = Author
		fields = ('username', 'password')
		widgets = {
			'username': TextInput(attrs = {'placeholder': 'username',}),
			'password': PasswordInput(attrs = {'placeholder': 'password',}),
		}

class UploadBot(ModelForm):
	class Meta:
		model = Bot
		exclude = ['rec_datetime','author','wins','loss','draw','ldrbrd_pos']
		widgets = {
			'Name': TextInput(attrs = {'placeholder': 'Name for bot'})
		}
		