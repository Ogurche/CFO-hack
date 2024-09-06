from django.shortcuts import render, redirect
from .forms import TextInputForm
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, Http404, JsonResponse

def text_input_view(request):
    form = TextInputForm()
    return render(request, 'text_box.html', {'form': form})

# Create your views here.
