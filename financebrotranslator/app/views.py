from django.shortcuts import render

from .forms import TranslateForm
from .utils import cohere_utils, link_utils, sp500_utils


# Create your views here.
def index(request):
    input_status = False
    translation = ""
    companies = set()
    raw_translation = ""

    if request.method == 'POST':
        if request.POST["action"] == "Translate":
            form = TranslateForm(request.POST)
            if form.is_valid() and (request.POST["text"] != ""):
                input_status = True
                raw_translation = cohere_utils.generate(request.POST["text"])
                translation = link_utils.add_definition_links(raw_translation)
                companies = sp500_utils.get_stocks(request.POST["text"])
        elif request.POST["action"] == "Clear Text":
            form = TranslateForm()
            input_status = False
            translation = ""
    else:
        form = TranslateForm()
        input_status = False
        translation = ""

    return render(request, 'index.html', {'form': form, 'input_status': input_status, 'translation': translation, 'raw': raw_translation, 'companies': companies})
