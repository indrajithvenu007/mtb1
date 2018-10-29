from django import forms

# from booking.models import ReservationModel

class SelectedSeatForm(forms.Form):
	CHOICES=(('SILVER','silver'),('GOLD','gold'),('PLATINUM','platinum'))
	t_class = forms.ChoiceField(choices=CHOICES, required=True)
	selected_seat = forms.IntegerField(required=True,max_value=10)