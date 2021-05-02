from django.db import models



from django.utils import timezone




# Create your models here.
class Meal(models.Model):
	meal_name = models.CharField(max_length=200)
	meal_notes = models.CharField(max_length=1000, blank=True)

	def __str__(self):
		return self.meal_name 


	
class Monday(models.Model):
	lunch = models.CharField(max_length=200, null=False)
	dinner = models.CharField(max_length=200, null=False)

	def __str__(self):
		return f'{self.lunch} and {self.dinner}'


class Tuesday(models.Model):
	lunch = models.CharField(max_length=200)
	dinner = models.CharField(max_length=200)

	def __str__(self):
		return f'{self.lunch} and {self.dinner}'


class Wednesday(models.Model):
	lunch = models.CharField(max_length=200)
	dinner = models.CharField(max_length=200)

	def __str__(self):
		return f'{self.lunch} and {self.dinner}'


class Thursday(models.Model):
	lunch = models.CharField(max_length=200)
	dinner = models.CharField(max_length=200)

	def __str__(self):
		return f'{self.lunch} and {self.dinner}'

class Friday(models.Model):
	lunch = models.CharField(max_length=200)
	dinner = models.CharField(max_length=200)

	def __str__(self):
		return f'{self.lunch} and {self.dinner}'

class Saturday(models.Model):
	lunch = models.CharField(max_length=200)
	dinner = models.CharField(max_length=200)

	def __str__(self):
		return f'{self.lunch} and {self.dinner}'

class Sunday(models.Model):
	lunch = models.CharField(max_length=200)
	dinner = models.CharField(max_length=200)

	def __str__(self):
		return f'{self.lunch} and {self.dinner}'

