from django.contrib import admin
from Management import models
from parse_rest.connection import register
from parse_rest.datatypes import Object


class Place(Object):
	pass

class PlaceAdmin(admin.ModelAdmin):

	def save_model(self, request, obj, form, change):
		register('MQRrReTdb9c82PETy0BfUoL0ck6xGpwaZqelPWX5','44mp6LNgEmYEfZMYZQz16ncu7oqcnncGFtz762nC')
		place = Place()
		place.name = obj.name
		place.photo = obj.photo
		place.phone = obj.phone
		place.category = obj.category
		place.open_hour = obj.open_hour
		place.latitude = obj.latitude
		place.longitude = obj.longitude
		place.news = obj.news
		place.description = obj.description
		place.save()

admin.site.register(models.Place,PlaceAdmin)
