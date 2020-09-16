from django.shortcuts import render
from django.http import HttpResponse
from .models import carauselImgs
from .models import Product
from .models import Clients
from .models import contact_us


# Create your views here.
def base(request):
    return render(request,'updateSystem/base.html')
def index(request):
    carausel = carauselImgs.objects.all()
    product = Product.objects.all()
    clients = Clients.objects.all()
    return render(request,'updateSystem/index.html',{'carausel':carausel[:],
                                                    'product123':product[:3],
                                                    'product456':product[3:6],
                                                    'product789':product[6:9],
                                                    'clients':clients[:]})
def home(request):
    carausel = carauselImgs.objects.all()
    product = Product.objects.all()
    clients = Clients.objects.all()
    return render(request,'updateSystem/home.html',{'carausel':carausel[:],
                                                    'product123':product[:3],
                                                    'product456':product[3:6],
                                                    'product789':product[6:9],
                                                    'clients':clients[:]})

def quickview(request,myid):
    product = Product.objects.filter(product_id=myid)
    print(product)
    return render(request,'updateSystem/quickview.html',{'prod':product})

def ContactUs(request):
    if request.method == "POST":
        fname = request.POST.get('fname','');
        lname = request.POST.get('lname','');
        email = request.POST.get('mail','');
        phone = request.POST.get('phone','');
        city = request.POST.get('city','');
        state = request.POST.get('state','');
        country = request.POST.get('country','');
        cname = request.POST.get('cname','');
        enquiry = request.POST.get('enquiry','');
        contact = contact_us(fname=fname,lname=lname,mail=email,phone=phone,city=city,state=state,country=country,cname=cname,enquiry=enquiry)
        contact.save()

        if fname=="" or lname == "" or email =="" or phone==" " or city == "" or state =="" or contact == " " or cname=="" or enquiry =="":
            return render(request,'updateSystem/Error.html')



    return render(request,'updateSystem/ContactUs.html')

def Abouts(request):
    return render(request,'updateSystem/AboutCtech.html')

def Error(request):
    return render(request,'updateSystem/Error.html')

def CSR(request):
    return render(request,'updateSystem/csr.html')



def Achievements(request):
    return render(request,'updateSystem/Achievments.html')