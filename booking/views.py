# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView,TemplateView
from booking.forms import SelectedSeatForm
from movies.models import ShowModel,ScreenModel
from booking.models import ReservationModel
from django.conf import settings

import stripe

# Create your views here.
stripe.api_key=settings.STRIPE_SECRET_KEY


class BookingAdd(TemplateView):
	template_name='booking_templates/addbooking.html'
	@method_decorator(login_required)
	def get(self,request,pk):
		s_id=pk
		show_details=ShowModel.objects.get(id=s_id)
		screen=show_details.screen
		screen_details=ScreenModel.objects.get(sc_name=screen)
		silver_price=screen_details.silver_price
		gold_price=screen_details.gold_price
		platinum_price=screen_details.platinum_price	
		gold_seats=screen_details.gold_seat
		platinum_seats=screen_details.platinum_seats
		form=SelectedSeatForm
		context = {'show_details':show_details,
		'screen':screen,
		'silver_price':silver_price,
		'gold_price':gold_price,
		'platinum_price':platinum_price,
		'gold_seats':gold_seats,
		'platinum_seats':platinum_seats,
		'form':form,

		}
		return render(request,self.template_name,context)

	def post(self,request,pk):
		s_id=pk
		show_details=ShowModel.objects.get(id=s_id)
		movie=show_details.movie
		screen=show_details.screen
		date=show_details.s_date
		time=show_details.s_time
		screen_details=ScreenModel.objects.get(sc_name=screen)
		s_seats_available=screen_details.silver_seats
		g_seats_available=screen_details.gold_seat
		p_seats_available=screen_details.platinum_seats
		s_price=screen_details.silver_price
		g_price=screen_details.gold_price
		p_price=screen_details.platinum_price


		if request.POST:
			ticket_class = request.POST.get('t_class')
			seats = request.POST.get('selected_seat')
			
			if ticket_class == 'SILVER':
				if int(s_seats_available)>=int(seats):
					tot=int(seats)*int(s_price)
					s_seats_available=int(s_seats_available)-int(seats)
					# ReservationModel.objects.create(ticket_price_per_ticket=s_price)
				else:
					print("seat not available")
			elif ticket_class =='GOLD':
				tot=int(seats)*int(g_price)
				g_seats_available=int(g_seats_available)-int(seats)
				# ReservationModel.objects.create(ticket_price_per_ticket=g_price)

			elif ticket_class=='PLATINUM':
				tot=int(seats)*int(p_price)
				p_seats_available=int(s_seats_available)-int(seats)
				# ReservationModel.objects.create(ticket_price_per_ticket=p_price)


			ReservationModel.objects.create(
                    user_data=request.user.username,
                    movie=movie,
                    screen=screen,
                	date=date,
                	show_time=time,
                	ticket_class=ticket_class,
                	no_seats=seats,
                	total_amt=tot
                )

			context={
					'movie':movie,
					'ticket_class':ticket_class,
					'seats':seats,
					'screen':screen,
					'date':date,
					'time':time,
					'tot':tot,
					's_seats_available':s_seats_available,
				
					}

		return render(request,self.template_name,context)

def payment(request):

	template_name='booking_templates/paymentpage.html'
	if request.POST:
		token=request.post['stripeToken']
		charge=stripe.Charge.create(
			amount=100,
			currency='USD',
			Description= 'charge',
			source=token
			)
		form.save()
	return render(request,template_name)


class OrderListView(ListView):
	template_name='order_lst_view.html'
	model=ReservationModel
	context_object_name ='o_list'