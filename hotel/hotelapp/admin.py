from django.contrib import admin
from .models import Customer,Hotel,Rooms,Reservation,Billing
from django import forms


class RoomsAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RoomsAdminForm,self).__init__(*args, **kwargs)

    def clean(self):
        room=self.cleaned_data.get('room_rate')
        if len(str(room)) > 7000:
            raise forms.ValidationError('please enter a valid rate,rate cannot be lesser than 7000 rupess',code='invalid')
        return self.cleaned_data

    def save(self, commit=True):
        return super(RoomsAdminForm,self).save(commit=commit)


class ReservationAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReservationAdminForm,self).__init__(*args, **kwargs)

    def clean(self):
        reserve=self.cleaned_data.get('noof_guest')
        if len(str(reserve)) < 5:
            raise forms.ValidationError('please enter a valid no of persons,persons cannot be greater than 5 persons',code='invalid')
        return self.cleaned_data

    def save(self, commit=True):
        return super(ReservationAdminForm,self).save(commit=commit)








# Register your models here.

class RoomsAdmin(admin.ModelAdmin):
    form=RoomsAdminForm
    list_display = ('room_type','room_rate',)
    list_filter = ('room_type',)
    search_fields = ('room_rate',)
    ordering = ('room_rate',)

class ReservationAdmin(admin.ModelAdmin):
    form=RoomsAdminForm
    search_fields = ("reservation_date",)
    ordering = ("reservation_date",)





admin.site.register(Rooms,RoomsAdmin)
admin.site.register(Reservation,ReservationAdmin)
admin.site.register(Hotel)
admin.site.register(Customer)
admin.site.register(Billing)




