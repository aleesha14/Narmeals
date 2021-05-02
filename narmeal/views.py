from django.shortcuts import render, redirect


from django.http import HttpResponse, HttpResponseRedirect


import datetime

from django.utils import timezone

from .models import Meal, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
from django.urls import reverse


def home(request):
    current_date = timezone.now()
    monday_meal = Monday.objects.get() 
    tuesday_meal = Tuesday.objects.get()
    wednesday_meal = Wednesday.objects.get()
    thursday_meal = Thursday.objects.get()
    friday_meal = Friday.objects.get()
    saturday_meal = Saturday.objects.get()
    sunday_meal = Sunday.objects.get()
    return render(request, 'narmeal/home.html', {
		'current_date':current_date,
		'monday_meal': monday_meal,
		'tuesday_meal': tuesday_meal,
		'wednesday_meal': wednesday_meal, 
		'thursday_meal': thursday_meal, 
		'friday_meal': friday_meal, 
		'saturday_meal': saturday_meal, 
		'sunday_meal': sunday_meal,
		})




def week_plan(request):
	current_date = timezone.now()
	meal_list = Meal.objects.all()
	monday_meal = Monday.objects.get() 
	tuesday_meal = Tuesday.objects.get()
	wednesday_meal=Wednesday.objects.get()
	thursday_meal = Thursday.objects.get()
	friday_meal = Friday.objects.get()
	saturday_meal = Saturday.objects.get()
	sunday_meal = Sunday.objects.get()
	return render(request, 'narmeal/week_plan.html', {
		'current_date':current_date,
		'meal_list': meal_list,
		'monday_meal':monday_meal,
		'tuesday_meal': tuesday_meal,
		'wednesday_meal': wednesday_meal, 
		'thursday_meal': thursday_meal, 
		'friday_meal': friday_meal, 
		'saturday_meal': saturday_meal, 
		'sunday_meal': sunday_meal,
		})

def choose_monday(request):
	monday_lunch = request.POST.get("monday1")
	monday_dinner = request.POST.get("monday2")
	

	print(monday_lunch)
	print(monday_dinner)

	if not Monday.objects.exists():
		saved_meal = Monday.objects.create(lunch=monday_lunch, dinner=monday_dinner)

		return HttpResponseRedirect(reverse('week_plan'))
	else:
		update_meal = Monday.objects.get()
		update_meal.lunch = monday_lunch
		update_meal.dinner = monday_dinner
		update_meal.save()

	
		return HttpResponseRedirect(reverse('week_plan'))

def choose_tuesday(request):
	tuesday_lunch = request.POST.get("tuesday1")
	tuesday_dinner = request.POST.get("tuesday2")

	print(tuesday_lunch)
	print(tuesday_dinner)

	if not Tuesday.objects.exists():
		saved_meal = Tuesday.objects.create(lunch=tuesday_lunch, dinner=tuesday_dinner)

		return HttpResponseRedirect(reverse('week_plan'))
	else:
		update_meal = Tuesday.objects.get()
		update_meal.lunch = tuesday_lunch
		update_meal.dinner = tuesday_dinner
		update_meal.save()

	
		return HttpResponseRedirect(reverse('week_plan'))

def choose_wednesday(request):
	wednesday_lunch = request.POST.get("wednesday1")
	wednesday_dinner = request.POST.get("wednesday2")



	if not Wednesday.objects.exists():
		saved_meal = Wednesday.objects.create(lunch=wednesday_lunch, dinner=wednesday_dinner)

		return HttpResponseRedirect(reverse('week_plan'))
	else:
		update_meal = Wednesday.objects.get()
		update_meal.lunch = wednesday_lunch
		update_meal.dinner = wednesday_dinner
		update_meal.save()

	
		return HttpResponseRedirect(reverse('week_plan'))

def choose_thursday(request):
	thursday_lunch = request.POST.get("thursday1")
	thursday_dinner = request.POST.get("thursday2")



	if not Thursday.objects.exists():
		saved_meal = Thursday.objects.create(lunch=thursday_lunch, dinner=thursday_dinner)

		return HttpResponseRedirect(reverse('week_plan'))
	else:
		update_meal = Thursday.objects.get()
		update_meal.lunch = thursday_lunch
		update_meal.dinner = thursday_dinner
		update_meal.save()

	
		return HttpResponseRedirect(reverse('week_plan'))

def choose_friday(request):
	friday_lunch = request.POST.get("friday1")
	friday_dinner = request.POST.get("friday2")



	if not Friday.objects.exists():
		saved_meal = Friday.objects.create(lunch=friday_lunch, dinner=friday_dinner)

		return HttpResponseRedirect(reverse('week_plan'))
	else:
		update_meal = Friday.objects.get()
		update_meal.lunch = friday_lunch
		update_meal.dinner = friday_dinner
		update_meal.save()

	
		return HttpResponseRedirect(reverse('week_plan'))

def choose_saturday(request):
	saturday_lunch = request.POST.get("saturday1")
	saturday_dinner = request.POST.get("saturday2")



	if not Saturday.objects.exists():
		saved_meal = Saturday.objects.create(lunch=saturday_lunch, dinner=saturday_dinner)

		return HttpResponseRedirect(reverse('week_plan'))
	else:
		update_meal = Saturday.objects.get()
		update_meal.lunch = saturday_lunch
		update_meal.dinner = saturday_dinner
		update_meal.save()

	
		return HttpResponseRedirect(reverse('week_plan'))

def choose_sunday(request):
	sunday_lunch = request.POST.get("sunday1")
	sunday_dinner = request.POST.get("sunday2")



	if not Sunday.objects.exists():
		saved_meal = Sunday.objects.create(lunch=sunday_lunch, dinner=sunday_dinner)

		return HttpResponseRedirect(reverse('week_plan'))
	else:
		update_meal = Sunday.objects.get()
		update_meal.lunch = sunday_lunch
		update_meal.dinner = sunday_dinner
		update_meal.save()

	
		return HttpResponseRedirect(reverse('week_plan'))









	


def meals_list(request):
	meal_list = Meal.objects.all().order_by("meal_name")
	num_meals = Meal.objects.all().count()
	#meal_list = ['chicken', 'plant', 'other stuff']
	return render(request, 'narmeal/meals_list.html', {
		'meal_list':meal_list,
		'num_meals':num_meals,
		})

def add_meal(request):
	return render(request, 'narmeal/add_meal.html')

def add(request):
	#print(request.POST)
	name = request.POST.get("content_1")
	notes = request.POST.get("content_2")
	print(name)
	print(notes)
	created_object = Meal.objects.create(meal_name=name.capitalize(), meal_notes=notes)
	print(created_object.id)
	return HttpResponseRedirect(reverse('meals_list'))
	

def delete_meal(request, meal_id):
	print(meal_id)
	Meal.objects.get(id=meal_id).delete()
	return HttpResponseRedirect(reverse('meals_list'))
		

def meal_view(request, meal_id):
	
	meal = Meal.objects.get(id=meal_id)
	return render(request, 'narmeal/meal_view.html', {
		'meal': meal

		})

def edit(request, meal_id):
	meal = Meal.objects.get(id=meal_id)
	return render(request, 'narmeal/edit_meal.html', {
		'meal':meal 
		})

def edit_meal (request, meal_id):
	edit_meal = Meal.objects.get(id=meal_id)
	edit_name = request.POST.get("edit_name")
	edit_notes = request.POST.get("edit_notes")
	edit_meal.meal_name = edit_name 
	edit_meal.meal_notes = edit_notes
	edit_meal.save()

	return HttpResponseRedirect(reverse('meals_list'))



	



