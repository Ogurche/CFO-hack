from django.db import models


# Create your models here.
class TextModel(models.Model):
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.text

class PDFModel(models.Model):
    pdf_file = models.FileField(upload_to='', verbose_name='PDF-файл')

    def __str__(self):
        return self.pdf_file.name