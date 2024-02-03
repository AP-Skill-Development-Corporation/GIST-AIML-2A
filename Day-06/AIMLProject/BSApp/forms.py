from .models import Student
from django import forms

class StForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = ["rn","sn","sy","sb"]
		widgets = {
		"rn":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Roll Number",
			}),
		"sn":forms.TextInput(attrs={
			"class":"form-control my-2",
			"placeholder":"Enter Student Name",
			}),
		"sy":forms.NumberInput(attrs={
			"class":"form-control my-2",
			"max":4,
			"min":1,
			}),
		"sb":forms.Select(attrs={
			"class":"form-control my-2",
			})
		}