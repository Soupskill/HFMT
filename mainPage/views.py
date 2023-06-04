from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from .models import QuestionModel


# Create your views here.
import requests




def getHomePage(request):

    header_template = 'header.html'
    footer_template = 'footer.html'
    head_template = 'head.html'
    if request.META.get('HTTP_HX_REQUEST'):
        header_template = 'empty_template.html' 
        footer_template = 'empty_template.html' 
        
    
        
    return render(
        request,
        "home.html",
        {'header_template': header_template,
        'footer_template': footer_template,
        'head_template': head_template}
        )



def getAboutPage(request):

    header_template = 'header.html'
    footer_template = 'footer.html'
    head_template = 'head.html'
    if request.META.get('HTTP_HX_REQUEST'):
        header_template = 'empty_template.html' 
        footer_template = 'empty_template.html' 
    
    return render(
        request,
        "about.html",
        {'header_template': header_template,
        'footer_template': footer_template,
        'head_template': head_template}
        )



def getContactsPage(request):
    
    header_template = 'header.html'
    footer_template = 'footer.html'
    head_template = 'head.html'
    if request.META.get('HTTP_HX_REQUEST'):
        header_template = 'empty_template.html' 
        footer_template = 'empty_template.html' 
    
    return render(
        request,
        "contactsPage.html",
        {'header_template': header_template,
        'footer_template': footer_template,
        'head_template': head_template}
        )

def addQuestion(request):
    
    if request.method == 'POST':
        pass
