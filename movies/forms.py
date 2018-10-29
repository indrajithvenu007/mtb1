from django import forms
from movies.models import MovieModel,ShowModel,ScreenModel,CarousalModel



class MovieForm(forms.ModelForm):
	class Meta:
		model=MovieModel
		exclude=('create_date',)

class ShowForm(forms.ModelForm):
	class Meta:
		model=ShowModel
		exclude=('create_date',)

class ScreenForm(forms.ModelForm):
	class Meta:
		model=ScreenModel
		exclude=('create_date',)



class CarousalForm(forms.ModelForm):
	class Meta:
		model=CarousalModel
		exclude=('create_date',)