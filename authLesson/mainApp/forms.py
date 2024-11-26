from django.forms import forms,CharField
class UserForm(forms.Form):
	username = CharField()
	password = CharField()
	first_name = CharField()
	last_name = CharField()
