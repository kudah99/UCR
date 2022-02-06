from django.contrib import admin
from  django.contrib.auth.models  import  Group
from .models import CustomersMessage
from .models import OurFleet
from .models import Customer
from .models import Bookings


class customersMessage(admin.ModelAdmin):
    list_display = ('name','email','subject','body')

class ourFleet(admin.ModelAdmin):
    list_display = ['vehicle_type']
    def active(self, obj):
        return obj.is_active == 1
  
    active.boolean = True

class customer(admin.ModelAdmin):
    list_display = ('first_name','last_name','title','gender','email','phone_number','createdAt')
    list_filter = ["createdAt"]
    search_fields = ('last_name__startswith',)

class bookings(admin.ModelAdmin):
    list_display = ('customer_title','customer_name','phone_number','vehicle_type', 'pick_up_Location','pick_up_time','drop_off_Location','drop_off_time','bookedOn')
    list_filter = ("bookedOn",)
    search_fields = ('customer_name__startswith',)
    

admin.site.register(CustomersMessage ,customersMessage)
admin.site.register(OurFleet, ourFleet)
admin.site.register(Customer,customer)
admin.site.register(Bookings, bookings)

admin.site.unregister(Group)