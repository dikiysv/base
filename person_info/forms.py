from django.forms import ModelForm
from django import forms
from person_info.models import Adres, Interest
from django.forms import widgets

class addadresForm(ModelForm):
	class Meta:
		model = Adres
		fields = ['adr']

class addVidsForm(forms.Form):
	interests = forms.ModelMultipleChoiceField(queryset = Interest.objects.all(), widget = forms.CheckboxSelectMultiple)