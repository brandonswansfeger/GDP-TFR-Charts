from django import forms
from django.forms import ModelForm
from .models import *



        
class IndicatorDataForm(ModelForm):
    class Meta:
        model = IndicatorData
        fields = ['year', 'indicator']
    

        

# class YearChoiceField(forms.Form):
#     FILTER_CHOICES_YEAR = (
#         ('year', '2010'),
#       )

#     filter_by = forms.ChoiceField(choices = FILTER_CHOICES_YEAR)
    
# class IndicatorChoiceField(forms.Form):    
#     FILTER_CHOICES_INDIC = (
#         ('YR2010', '2010'),
#       )

#     filter_by = forms.ChoiceField(choices = FILTER_CHOICES_YEAR)
    
   
#     def clean(self):
#     # It will validate data
#         self.cleaned_data = super().clean()
#     # do what you want
#         return self.cleaned_data
