from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.dates import MonthArchiveView
from .models import Archive

# Create your views here
@login_required(login_url="login/")
def home(request):
    return render(request,"home.html")

class ArchiveMonthArchiveView(MonthArchiveView):
	queryset = Archive.objects.all()
	date_field = "pub_date"
	allow_future = True


def model_form_upload(request):
    if request.method =='POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UploadForm()
    return render(request,'core/form_upload.html',{'form':form})

    
