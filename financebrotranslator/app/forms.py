from django import forms

class TranslateForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows":"22", "cols":"88", "placeholder":"Type any \
text or use the microphone to recieve assistance"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""
            field.required = False
