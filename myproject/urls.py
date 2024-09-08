"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.add_text_and_pdf, name='main_page'),
    # path('add_text/', views.add_text, name='add_text'),
    # path('add_pdf/', views.add_pdf, name='add_pdf'),
    path('complete/', views.complite, name='complite'),
    # path('page2/', views.pages, name='page2'),
]   


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)