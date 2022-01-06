from django.http import response
from django.http.response import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
import matplotlib.pyplot as plt
import io
import urllib, base64
from .utils import get_plot
from .models import IndicatorData
from .forms import IndicatorDataForm




# Create your views here.


def barchart(request):
    form2 = IndicatorDataForm(request.POST or None)
    if request.method == 'POST':
        if form2.is_valid():
            form2.save('indicator')
    else:
        form2 = IndicatorDataForm()
        # yr = [yr.YearChoiceField for yr in data]
    # indic = [indic.indicatorChoiceField for indic in data2]
    p = IndicatorData.objects.last()
    yearselected = p.year
    indicatorselected = p.indicator
    yearonly = yearselected[2:]
    chart=get_plot(yearselected, indicatorselected)
    
    context={
      
        'chart':chart,
        'form2':form2,
        'yearonly':yearonly,
       
    }
   
    return render(request, 'gnibarchart/barchart.html', context )

    

def index(request):
    form2 = IndicatorDataForm(request.POST or None)
    if request.method == 'POST':
        if form2.is_valid():
            form2.save('indicator')
            return  redirect('barchart/')
    else:
        form2 = IndicatorDataForm()
        # yr = [yr.YearChoiceField for yr in data]
    # indic = [indic.indicatorChoiceField for indic in data2]
    # p = IndicatorData.objects.last()
    # yearselected = p.year
    # indicatorselected = p.indicator
    # yearonly = yearselected[2:]
    # chart=get_plot(yearselected, indicatorselected)
    
    context={
      
        # 'chart':chart,
        'form2':form2,
        # 'yearonly':yearonly,
       
    }
   
    return render(request, 'gnibarchart/index.html', context )
