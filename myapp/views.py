from django.shortcuts import render, redirect
from .forms import TextForm, PDFForm, InputForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, Http404, JsonResponse
from .models import PDFModel

import datetime
import os

# def add_text(request):
#     if request.method == 'POST':
#         form = TextForm(request.POST)
#         if form.is_valid():
#             # form.save()
#             return redirect('complite')
#     else:
#         form = TextForm()
#     return render(request, 'add_text.html', {'form': form})

# def add_pdf(request):
#     if request.method == 'POST':
#         form = PDFForm(request.POST, request.FILES)
#         if form.is_valid():
            
#             form.save()
#             return redirect('complite')
#     else:
#         form = PDFForm()
#     return render(request, 'add_pdf.html', {'form': form})
# Create your views here.

def add_text_and_pdf(request):
    if request.method == 'POST':
        form = InputForm(request.POST, request.FILES)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            pdf_file = form.cleaned_data.get('pdf_file')
            # if text:
                # TextModel.objects.create(text=text)
            if pdf_file:

                unix_timestamp = int(datetime.datetime.now().timestamp())
                filename, file_extension = os.path.splitext(pdf_file.name)
                filename = f"{unix_timestamp}_inputfile.{file_extension}"
                pdf_file.name = filename
                PDFModel.objects.create(pdf_file=pdf_file)
                # PDFModel.objects.create(pdf_file=pdf_file)
            return redirect('complite')
    else:
        form = InputForm()
    return render(request, 'add_text_pdf.html', {'form': form})

def complite(request):
    return render(request, 'complite.html')


def main_page (request):
    return render(request, 'main_page.html')