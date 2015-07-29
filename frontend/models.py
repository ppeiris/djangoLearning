from django.db import models
from django.contrib.auth.models import User
import datetime

# Define the tables


class Profile(models.Model):
	name = models.CharField(max_length = 128, unique = True)

	def __unicode__(self):
		return self.name

class Address(models.Model):
	profile_id = models.ForeignKey(Profile)
	address1 = models.CharField(max_length = 128)
	address2 = models.CharField(max_length = 128, blank = True)
	city = models.CharField(max_length = 128)
	zipcode = models.IntegerField(default = 0)
	state = models.CharField(max_length = 2)
	dateCreated = models.DateField(auto_now_add = True)

	def __unicode__(self):
		return self.address1 + self.address2



class UserProfile(models.Model):
	user = models.OneToOneField(User)

	picture = models.ImageField(upload_to='profile_images', blank=True)

	def __unicode__(self):
		return self.user.username



