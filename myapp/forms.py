from django import forms
from .models import TextModel, PDFModel

class InputForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, required=False)
    pdf_file = forms.FileField(required=False)
    

class TextForm(forms.ModelForm):
    class Meta:
        model = TextModel
        fields = ('text',)
        text = forms.CharField(widget=forms.Textarea)

class PDFForm(forms.ModelForm):
    class Meta:
        model = PDFModel
        fields = ('pdf_file',)