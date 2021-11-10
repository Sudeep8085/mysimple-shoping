from django.shortcuts import render
# select * from product
# ORM
# Product.objects.all() # Queryset[]
# Product.objects.filter() # Queryset[]

# Create your views here.
from .models import Product,MainCat,SubCat
def home(request):
    mydict={}
    p=Product.objects.all()
    maincat=MainCat.objects.all()
    subcat=SubCat.objects.all()

    mydict['records']=p
    mydict['maincat']=maincat
    mydict['subcat']=subcat

    return render(request,'home.html',mydict)

def details(request,pid=None):
    mydict={}
    p =Product.objects.get(id=pid)
    mydict['p']=p
    return render(request,'pro_details.html',mydict)