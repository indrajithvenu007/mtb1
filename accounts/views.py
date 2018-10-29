# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.shortcuts import render,redirect


from django.views.generic import FormView,ListView
from django.contrib.auth.models import User
from accounts.forms import UserForm, CustomerForm
from accounts.models import Customer



import requests

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages

from .models import Comment
from .forms import CommentForm

# Create your views here.


class UserAdd(FormView):
	template_name = 'customer_details/userreg.html'
	form_class = UserForm
	model = User
	# success_url='/home'
	def get(self,request,*args,**kwargs):
		self.object = None
		form_class = self.get_form_class()
		user_form = self.get_form(form_class)
		cust_form = CustomerForm()
		return self.render_to_response(self.get_context_data(form1=user_form,form2=cust_form))

	def post(self,request,*args,**kwargs):
		self.object = None
		form_class = self.get_form_class()
		user_form = self.get_form(form_class)
		cust_form = CustomerForm(self.request.POST, self.request.FILES)
		if (user_form.is_valid() and cust_form.is_valid()):
			return self.form_valid(user_form, cust_form)
		else:
			return self.form_invalid(user_form, cust_form)

	def get_success_url(self, **kwargs):
		return ('success')

	def form_valid(self, user_form, cust_form):
		self.object = user_form.save()
		self.object.is_staff=True
		self.object.save()
		cust_obj = cust_form.save(commit=False)
		cust_obj.user_data = self.object
		cust_obj.save()
		return redirect('/home/')

	def form_invalid(self, user_form, cust_form):
		return self.render_to_response(self.get_context_data(form1=user_form,form2=cust_form))



class UserListView(ListView):
	template_name='customer_details/user_lst_view.html'
	model=User
	context_object_name ='u_list'

def login(request):
     form =AuthenticationForm()
     if request.user.is_authenticated():
         if request.user.is_superuser:
             return redirect("/home/")# or your url name
         if request.user.is_staff:
             return redirect("/home/")# or your url name


     if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')
         user = auth.authenticate(username=username, password=password)

         if user is not None:
             # correct username and password login the user
             auth.login(request, user)
             if request.user.is_superuser:
                 return redirect("/home/")# or your url name
             if request.user.is_staff:
                 return redirect("/home")# or your url name

         else:
             print 'Error wrong username/password'
     context = {}
     context['form']=form

     return render(request, 'customer_details/login.html', context)




def comments(request):
    comments_list = Comment.objects.order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():

            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            ''' End reCAPTCHA validation '''

            if result['success']:
                form.save()
                messages.success(request, 'New comment added with success!')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')

            return redirect('comments')
    else:
        form = CommentForm()

    return render(request, 'core/comments.html', {'comments': comments_list, 'form': form})