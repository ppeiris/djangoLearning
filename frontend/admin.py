from django.contrib import admin
from frontend.models import Profile, Address, UserProfile

class AddressAdmin(admin.ModelAdmin):
	list_display = ('address1',  'address2',  'city',  'zipcode',  'state',  'dateCreated')

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('id', 'picture', 'user_id')

admin.site.register(Profile)
admin.site.register(Address, AddressAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
