        
from django.shortcuts import render,HttpResponse,redirect
from pathlib import Path

from .models import myuploadfile

# Create your views here.
def index(request):
    context = {
        "data":myuploadfile.objects.all(),
    }
    return render(request,"index.html",context)

def send_files(request):
    data = request.FILES
    if request.method == "POST" :        
        myfile = data.getlist("uploadfiles")
        
        for f in myfile:
            path = f.name
            myuploadfile(
                f_name = Path(path).stem, 
                myfiles = f
            ).save()
            
        
        return redirect("fileapp:index")


        