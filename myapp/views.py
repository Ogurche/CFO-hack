import tempfile
from django.shortcuts import render, redirect
import xhtml2pdf.document
from .forms import TextForm, PDFForm, InputForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, Http404, HttpResponseNotFound, JsonResponse
from .models import PDFModel
from .processing import process_doc_file
from django.template.loader import render_to_string
# import pdfkit
# from xhtml2pdf import pisa 
# from django.template.loader import get_template
from io import BytesIO
# from easy_pdf.views import PDFTemplateView

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
        # return redirect('complite')


    test_json = {
        'data': {
            'key1': 'asdas., dzxc',
            'key2': 'asf.,asmfфывфывфывфывыфвфывфывфывфывыфв.',
            'key3': 'lksdaflask',
            'key4': 'ывжэда',
            'key5': 'zxc,mas dfna,mфывпфриттьф ырпвфыодвлфывлф'
        },
        'Название': 'Аналитика',
        'pages': [
            {'title': 'Page 1', 'template': 'slides/page1.html'},
            {'title': 'Page 2', 'template': 'slides/page2.html'},
            {'title': 'Page 3', 'template': 'slides/page3.html'},
            {'title': 'Page 4', 'template': 'slides/page4.html'}
        ]
    }
    pages =[]
    for page in test_json['pages']:
        html_content = render(request=request, template_name=page['template']
                              , context={'data': test_json['data']
                                         , 'Название': test_json['Название']}).content.decode('utf-8')
        pages.append(html_content)   

    return render(request, 'text_box.html', context={'pages': pages})    

def pages (request):
    test_json = {
        'data': {
            'key1': 'asdas., dzxc',
            'key2': 'asf.,asmfфывфывфывфывыфвфывфывфывфывыфв.',
            'key3': 'lksdaflask',
            'key4': 'ывжэда',
            'key5': 'zxc,mas dfna,mфывпфриттьф ырпвфыодвлфывлф'
        },
        'Название': 'Аналитика',
        'pages': [
            {'title': 'Page 1', 'template': 'slides/page1.html'},
            {'title': 'Page 2', 'template': 'slides/page2.html'},
            {'title': 'Page 3', 'template': 'slides/page3.html'},
            {'title': 'Page 4', 'template': 'slides/page4.html'}
        ]
    }
    pages =[]
    for page in test_json['pages']:
        html_content = render(request=request, template_name=page['template']
                              , context={'data': test_json['data']
                                         , 'Название': test_json['Название']}).content.decode('utf-8')
        pages.append(html_content)   
    # page_key = test_json['Название']  # Get the first key from the test_json dictionary
    # if page_key == 'Аналитика':
    #     html_template = 'slides/page2.html'
    # elif page_key == 'Другое':
    #     html_template = 'slides/page3.html'
    # elif page_key == 'Третье':
    #     html_template = 'slides/page4.html'
    # else:
    #     # Handle the case where the key is neither 'page1' nor 'page2'
    #     return HttpResponseNotFound('Page not found')

    # html_content = render(request=request, template_name= html_template, context={'data':test_json['data'], 'Название':test_json['Название']})
    
    return render(request, 'text_box.html', context={'pages': pages})    
    # response = HttpResponse(pdf_buffer.getvalue(),content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename="output.pdf"'
    # return response

def complite(request):
    return render(request, 'complite.html')


def main_page (request):
    return render(request, 'main_page.html')