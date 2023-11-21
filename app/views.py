from django.shortcuts import render

# Create your views here.


def data_render(request):
    data='This data is our assumption'
    d={'assumption':data,'name':'Ramesh','age':23}
    return render(request,'data_render.html',context=d)
