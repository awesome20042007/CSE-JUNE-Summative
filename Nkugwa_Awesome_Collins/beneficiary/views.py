from django.shortcuts import render, redirect
from .forms import BeneficiaryForm


# Create your views here.
def landing(request):
    return render(request, 'landing.html')


def register(request):
    success = False

    if request.method == 'POST':
        form = BeneficiaryForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = BeneficiaryForm()
    else:
        form = BeneficiaryForm()

    return render(request, 'register.html', {'form': form, 'success': success})