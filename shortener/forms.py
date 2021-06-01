from django import forms
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
 

class ShortenURLForm(forms.Form):
	url = forms.URLField(
		label='',
		widget=forms.TextInput(
			attrs={
				'placeholder': 'Long URL',
				'class': 'form-control'
			}
		)
	)
