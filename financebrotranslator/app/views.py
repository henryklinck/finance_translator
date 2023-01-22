from django.shortcuts import render

from .forms import TranslateForm
from .utils import cohere_utils, link_utils


# Create your views here.
def index(request):
    input_status = False
    translation = ""

    if request.method == 'POST':
        if request.POST["action"] == "Translate":
            form = TranslateForm(request.POST)
            if form.is_valid() and (request.POST["text"] != ""):
                input_status = True
                raw_translation = cohere_utils.generate(request.POST["text"])
                translation = link_utils.add_definition_links(raw_translation)
        elif request.POST["action"] == "Clear Text":
            form = TranslateForm()
            input_status = False
            translation = ""
    else:
        form = TranslateForm()
        input_status = False
        translation = ""

    return render(request, 'index.html', {'form': form, 'input_status': input_status, 'translation': translation, 'raw': raw_translation})
