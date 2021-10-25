from django.shortcuts import redirect, render

from dashboard.models import Data
from .forms import DataForm
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-predictions')
    else:
        form = DataForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/index.html', context)


def predictions(request):
    predictions_sports = Data.objects.all()
    context = {
        'predictions_sports':predictions_sports
    }
    return render(request, 'dashboard/predictions.html', context)