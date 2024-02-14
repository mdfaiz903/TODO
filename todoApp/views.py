from django.shortcuts import render,HttpResponse
from  . forms import todoForm
# Create your views here.
def home(request):
    form = todoForm()


    return render(request,'todoApp/index.html',{'frm':form})