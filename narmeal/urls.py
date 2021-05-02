from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('meals', views.meals_list, name='meals_list'),
    path('week_plan', views.week_plan, name='week_plan'),
    path('monday', views.choose_monday, name='monday'),
    path('tuesday', views.choose_tuesday, name='tuesday'),
    path('wednesday', views.choose_wednesday, name='wednesday'),
    path('thursday', views.choose_thursday, name='thursday'),
    path('friday', views.choose_friday, name='friday'),
    path('saturday', views.choose_saturday, name='saturday'),
    path('sunday', views.choose_sunday, name='sunday'),
    path('add_meal', views.add_meal, name='add_meal'),
    path('meal_view/edit/<int:meal_id>', views.edit, name='edit'),
    path('edit_meal/<int:meal_id>', views.edit_meal, name='edit_meal'),
    path('add', views.add, name='add'),
    path('delete_meal/<int:meal_id>' , views.delete_meal, name='delete_meal'),
    path('meal_view/<int:meal_id>', views.meal_view, name='meal_view'),
]