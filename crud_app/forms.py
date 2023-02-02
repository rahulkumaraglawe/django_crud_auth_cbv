from django import forms
from .models import Hotel
from django.core import validators


class HotelForm(forms.ModelForm):

    room = forms.IntegerField(label = 'ROOM NO', validators=[validators.MinValueValidator(101)])
    
    class Meta:
        model = Hotel
        fields = '__all__'
        
        
        labels = {
            'name':'CUSTOMER NAME',
            'cdate':'CHECK-IN DATE'
        }
        
        
        widgets = {
            'cdate':forms.DateInput(attrs = {
                'type':'date'
            })
        }