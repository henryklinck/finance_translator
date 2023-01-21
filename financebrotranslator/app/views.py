from django.shortcuts import render

from .forms import TranslateForm

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = TranslateForm(request.POST)
        if form.is_valid():
            print(request.POST)
    else:
        form = TranslateForm()

    return render(request, 'index.html', {'form': form})
