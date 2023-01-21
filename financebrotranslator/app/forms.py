from django import forms

class TranslateForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows":"25", "cols":"100"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""
            field.required = False
