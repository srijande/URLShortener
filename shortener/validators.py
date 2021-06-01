from django.core.exceptions import ValidationError

def validate_com_url(value):
	if 'com' not in value:
		raise ValidationError("Entered URL is not a valid .com url")
	return value
