from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from  . forms import todoForm
from . models import todo_model
from django .contrib import messages
# Create your views here.
def home(request):
    data = todo_model.objects.all().order_by('-id')
    
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


    return render(request,'todoApp/index.html',{'data':data,'frm':form})



def deleteview(request,id):
    delete_item = get_object_or_404(todo_model,id=id)
    if delete_item:
        delete_item.delete()
        messages.success(request,f"List No {id} is deleted successfully")
        return redirect('home') 
    

def updateview(request,id):
    update_text = todo_model.objects.get(id=id)

    form = todoForm(request.POST or None , instance = update_text)
    if form.is_valid():
        form.save()
        return redirect("home")

    return render(request,'todoApp/update.html',{'form':form})
