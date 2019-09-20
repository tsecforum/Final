from django.contrib import admin
from .models import NGO,Events
# Register your models here.
class NGOAdmin(admin.ModelAdmin):

	list_display = {'id','title','city','state','is_verified','post_date'}
	list_display_links = {'id','title'}
	list_display = {'is_verified'}
	list_filter = {'city','state'}
	search_fields = {'title','description','city','state'}

admin.site.register(NGO,NGOAdmin)

class EventsAdmin(admin.ModelAdmin):

	list_display = {'id','title','location','post_date','amount'}
	list_display_links = {'id','title'}
	search_fields = {'title','description','location'}

admin.site.register(Events,EventsAdmin)
