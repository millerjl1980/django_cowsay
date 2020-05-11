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
            new_cow.output = output
            new_cow.save()
            return render(request, 'index.html', {'form': TextForm, 'cow': output})
    else:
        form = TextForm()
    return render(request, 'index.html', {'form': TextForm})