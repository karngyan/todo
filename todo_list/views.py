from django.shortcuts import render , redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

from datetime import datetime

def home(request):

	my_date = datetime.now()

	if request.method == 'POST':
		form = ListForm(request.POST or None)
		all_items = List.objects.all

		if form.is_valid():
			form.save()
			all_items = List.objects.all
			messages.success(request , ('Item Has Been Added To List!'))
		return render(request , 'home.html' , {'all_items': all_items , 'my_date': my_date})
		
	else:
		all_items = List.objects.all
		return render(request , 'home.html' , {'all_items': all_items , 'my_date': my_date})

def delete(request , list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.success(request, ('Item Has Been Deleted'))
	return redirect('home')

def cross_off(request , list_id):
	item = List.objects.get(pk=list_id)
	item.completed = True
	item.save()
	return redirect('home')

def uncross(request, list_id):
	item = List.objects.get(pk=list_id)
	item.completed = False
	item.save()
	return redirect('home')

def edit(request , list_id):
	if request.method == 'POST':
		item = List.objects.get(pk=list_id)

		form = ListForm(request.POST or None , instance=item)

		if form.is_valid():
			form.save()
			messages.success(request , ('Item Has Been Edited!'))
			return redirect('home')
	else:
		item = List.objects.get(pk=list_id)
		return render(request , 'edit.html' , {'item' : item})
