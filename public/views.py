from django.shortcuts import render
from .forms import BookingForm

def  index(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    form = BookingForm()
    return render(request, 'public/index.html',{'form': form})