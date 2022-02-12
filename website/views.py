from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm,Contact_form, NewsLetterForm
def index_view(request):
    return render(request , 'website/index.html')

def about_view(request):
    return render(request , "website/about.html")

def contact_view(request):
    if request.method == 'POST':
        form = Contact_form(request.POST)
        if form.is_valid():
            form.save()
    form = Contact_form()
    return render(request , "website/contact.html", {'form':form})


def newsLetter_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
    else:
                return HttpResponseRedirect('/')







# def test_view(request):
#     if request.method == 'POST':
#         form = Contact_form(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('done')
#         else:
#             return HttpResponse('not valid')
#     form = Contact_form()
#     return render(request ,'test.html' , {'form':form})
