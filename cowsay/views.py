from django.shortcuts import render
from cowsay.models import Cow
from cowsay.forms import TextForm
import subprocess

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            new_cow = form.save()
            # https://www.youtube.com/watch?v=2Fp1N6dof0Y
            output = subprocess.run(['cowsay', new_cow.text], capture_output=True, text=True)
            output = output.stdout
            return render(request, 'index.html', {'form': TextForm, 'output': output})
    else:
        form = TextForm()
    return render(request, 'index.html', {'form': TextForm})

def old_cows(request):
    # https://stackoverflow.com/questions/20555673/django-query-get-last-n-records
    last_ten = Cow.objects.all().order_by('-id')[:10]
    old_cows = []
    for cow in last_ten:
        output = subprocess.run(['cowsay', cow.text], capture_output=True, text=True)
        old_cows.append(output.stdout)
    return render(request, 'old_cows.html', {'old_cows': old_cows})