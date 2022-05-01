

from django.http import HttpResponse
from django.shortcuts import render
from clouds.models import Contact
from . import views
# from clouds.forms import imageuploader


def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')
    
def index(request):
    return render(request,'index.html')
    
def contact(request):
    n = ''
    if request.method=='POST': 
        name = request.POST.get('name')
        email  = request.POST.get( 'email')      
        phone     = request.POST.get( 'phone')     
        age  = request.POST.get('age')   
        date_of_birth    = request.POST.get('date_of_birth')   
        disc       = request.POST.get('disc')   
        data = Contact(name=name,email=email,phone=phone,age=age,date_of_birth=date_of_birth,disc=disc)
        data.save()
        n = 'aap ka data ja chuka hey wahan check karain bhai '
    return render(request,"info.html",{'n':n})


def services(request):
    return render(request,'services.html')

def imageuploader(request):
    return render(request,'imageuploader.html')


# def imageuploader(request):        
#         if request.method == "POST":
#             form = image(request.POST , request.FILES)
#             if form.is_valid():
#                 form.save()
#                 form = image()
#                 img = Image.objects.all
#         return render(request,'imageuploader.html',{'img':img,'form':form)
# def MDuniform(request):
#     n = ''
#     if request.method=='POST': 
#         shirt = request.POST.get('shirt')
#         Banyan  = request.POST.get( 'Banyan')      
#         pent     = request.POST.get( 'pent')     
#         underware  = request.POST.get('underware')   
#         sweater    = request.POST.get('sweater')   
#         tie        = request.POST.get('tie')  
#         data = uniform(shirt=shirt,Banyan=Banyan,pent=pent,underware=underware,sweater=sweater,tie=tie)
#         data.save()
#         n = 'aap ka data ja chuka hey wahan check karain bhai samjhay data inserted'
#     return render(request,"contact.html",{'n':n})



def info(request):
    return render(request,'info.html')