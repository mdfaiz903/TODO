from django.shortcuts import render,HttpResponse
from  . forms import todoForm
from . models import todo_model
from django .contrib import messages
# Create your views here.
def home(request):
    if request.method =='POST':
        form = todoForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, "Items Added Successfully")

        except:
            raise ValueError("Invalid or Empty Fields")
    else:
        form = todoForm()


    return render(request,'todoApp/index.html',{'frm':form})