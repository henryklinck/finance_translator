from django.shortcuts import render

from .forms import TranslateForm
from .utils import cohere_utils

# Create your views here.
def index(request):
    input_status = False
    translation = ""

    if request.method == 'POST':
        form = TranslateForm(request.POST)
        if form.is_valid():
            input_status = True
            print(request.POST["text"])
            translation = cohere_utils.generate(request.POST["text"])
    else:
        form = TranslateForm()
        input_status = False
        translation = ""

    return render(request, 'index.html', {'form': form, 'input_status': input_status, 'translation': translation})
