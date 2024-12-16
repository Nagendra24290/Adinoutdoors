from django.shortcuts import render
from django.http import HttpResponse
from adinapp.models import Advertisement
from adinapp.forms import BookingForm
from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd


# Create your views here.





def booking_page(request):
    ads = Advertisement.objects.all()
    return render(request, 'index.html', {'ads': ads})

def submit_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'Booking submitted successfully!'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'message': 'Invalid request'})

from django.core.paginator import Paginator
from adinapp.models import Ad

def ad_list_view(request):
    ads = Ad.objects.all()
    paginator = Paginator(ads, 12)  # 12 ads per page
    page_number = request.GET.get('page')
    ads_page = paginator.get_page(page_number)
    return render(request, 'index.html', {'ads': ads_page})
