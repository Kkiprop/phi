# views.py
from django.shortcuts import render, redirect
from .forms import DataForm, OtppForm

def collect_data(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # After successful submission
    else:
        form = DataForm()
    return render(request, 'collect_data.html', {'form': form})


def collect_otp(request):
    if request.method == 'POST':
        form = OtppForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')
    else:
        form = OtppForm()
    return render(request, 'collect_otp.html', {'form': form})


def thank_you(request):
    return render(request, 'thankyou.html')

def home(request):
    return render(request, 'landing.html')
