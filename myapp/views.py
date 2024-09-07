from django.shortcuts import render, redirect
from .forms import TextForm, PDFForm, InputForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, Http404, JsonResponse
from .models import PDFModel
from .processing import process_doc_file


import datetime
import os

def add_text_and_pdf(request):
    if request.method == "POST" and request.FILES.get('file'):
        file = request.FILES['file']

        unix_timestamp = int(datetime.datetime.now().timestamp())
        filename, file_extension = os.path.splitext(file.name)
        filename = f"{unix_timestamp}_inputfile{file_extension}"
        file.name = filename
        pdf_model_instance = PDFModel.objects.create(pdf_file=file)

        file_location = pdf_model_instance.pdf_file.path
        process_doc_file(file_location)

        return redirect('complite')

    return render(request, 'text_box.html')

def complite(request):
    return render(request, 'complite.html')


def main_page (request):
    return render(request, 'main_page.html')