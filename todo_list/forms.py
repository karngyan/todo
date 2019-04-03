from django import forms
from .models import List

class ListForm(forms.ModelForm):
	class Meta:
		model = List
		fields= ['item' , 'completed' , 'date_time']