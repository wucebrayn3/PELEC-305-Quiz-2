from django.shortcuts import render
from .forms import EventRegistrationForm
from .models import EventRegistration

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = EventRegistrationForm()
    
    return render(request, 'register.html', {'form': form})

def show_registrations(request):
    registrations = EventRegistration.objects.all()
    return render(request, 'registry.html', {'registrations': registrations})