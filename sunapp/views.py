from django.shortcuts import render, redirect
from sunapp.forms import ImageForm
from sunapp.models import Image 

def index(request):
    #new one line below
    #images = Image.objects.all()
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            #return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
            return redirect('/home')
    else:
        form = ImageForm()
    return render(request, 'index.html', {'form': form})
    #return render(request, 'home.html', {'images': images})

def home(request):
    images = Image.objects.all()
    return render(request, 'home.html', {'images': images})

def about(request):
    return render(request, 'about.html')