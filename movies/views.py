# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import CreateView,ListView,DetailView,UpdateView,TemplateView,DeleteView,View

from movies.forms import MovieForm,ShowForm,ScreenForm,CarousalForm
from movies.models import MovieModel,ShowModel,ScreenModel,CarousalModel
# from booking.forms import BookingForm

# Create your views here.

# class BaseView(View):
# 	template_name='base.html'
# 	queryset=MovieModel.objects.filter(m_status=1)
# 	def get_context_data(self, *args, **kwargs):
# 		context = super(MovieListHome, self).get_context_data(*args, **kwargs)
# 		context['screen_names'] = ScreenModel.objects.filter(sc_status=1)	
# 		# context['movie_names'] = MovieModel.objects.filter(m_status=1)	
# 		return context

class MovieAdd(CreateView):
	template_name='addmovies.html'
	form_class=MovieForm
	success_url='movie added'

class MovieListView(ListView):
	template_name='movie_lst_view.html'
	model=MovieModel
	context_object_name ='m_list'

class MovieListHome(ListView):
	template_name='index.html'
	queryset=MovieModel.objects.filter(m_status=1)
	def get_context_data(self, *args, **kwargs):
		context = super(MovieListHome, self).get_context_data(*args, **kwargs)
		context['screen_names'] = ScreenModel.objects.filter(sc_status=1)	
		context['carousal']=CarousalModel.objects.filter(sc_status=1)
		return context



class MovieDetail(DetailView):
	template_name='moviedetail.html'
	def get(self,request,pk):
		m_id=pk
		m_detail= MovieModel.objects.get(id=m_id)
		s_detail= ShowModel.objects.filter(movie=m_id).order_by('s_date').filter(s_status=1)
		date_list=[]
		s_date=s_detail[0].s_date
		for i in range(0, len(s_detail)):
			if s_date == s_detail[i].s_date:
				s_date = s_detail[i].s_date
			else:
				date_list.append(s_date)
				s_date = s_detail[i].s_date
		date_list.append(s_date)
		context={
            'm_detail':m_detail,
            's_detail':s_detail,
            'date_list': date_list,
        }
		return render(request,self.template_name,context)



class UpdateMovie(UpdateView):
	model=MovieModel
	form_class=MovieForm
	template_name='movie_update.html'
	context_object_name='m_update'
	success_url='/mlstview/'

class DeleteMovie(DeleteView):
	model=MovieModel
	form_class=MovieForm
	template_name='movie_delete.html'
	context_object_name='m_delete'
	success_url='/mlstview/'

class ShowAdd(CreateView):
	template_name='addshows.html'
	form_class=ShowForm
	success_url='show added'

class ShowListView(ListView):
	template_name='show_lst_view.html'
	model=ShowModel
	context_object_name ='s_list'

class UpdateShow(UpdateView):
	model=ShowModel
	form_class=ShowForm
	template_name='show_update.html'
	context_object_name='s_update'
	success_url='/slview/'

class DeleteShow(DeleteView):
	model=ShowModel
	form_class=ShowForm
	template_name='show_delete.html'
	context_object_name='s_delete'
	success_url='/slview/'

class ShowDetail(DetailView):
 	model=ShowModel
 	template_name='moviedetail.html'
	context_object_name='s_detail'

class ScreenAdd(CreateView):
	template_name='addscreen.html'
	form_class=ScreenForm
	success_url='screen added'

class ScreenListView(ListView):
	template_name='screen_lst_view.html'
	model=ScreenModel
	context_object_name ='sc_list'

class UpdateScreen(UpdateView):
	model=ScreenModel
	form_class=ScreenForm
	template_name='screen_update.html'
	context_object_name='sc_update'
	success_url='/sclview/'

class DeleteScreen(DeleteView):
	model=ScreenModel
	form_class=ScreenForm
	template_name='screen_delete.html'
	context_object_name='sc_delete'
	success_url='/sclview/'


class CarousalAdd(CreateView):
	template_name='addcarousal.html'
	form_class=CarousalForm
	success_url='carousal img  added'


class CarousalListView(ListView):
	template_name='carousal_lst_view.html'
	model=CarousalModel
	context_object_name ='c_list'

class UpdateCarousal(UpdateView):
	model=CarousalModel
	form_class=CarousalForm
	template_name='carousal_update.html'
	context_object_name='c_update'
	success_url='/clstview/'
