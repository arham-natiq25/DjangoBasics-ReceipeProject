from django.shortcuts import render,redirect
from .models import *
# Create your views here.


def receipes(request):
    if request.method =="POST":
        data = request.POST

        image = request.FILES.get('image')
        name = data.get('name', '')  # Set a default value for `name` in case it's not found
        description = data.get('description', '')  # Set a default value for `description`

        Receipe.objects.create(
            receipe_name=name,
            receipe_description=description,
            receipe_image=image
        )
        return redirect('/receipes/')
    
    querySet=Receipe.objects.all()
    # icontains  specific keyword of django
    if request.GET.get('search'):
        querySet = querySet.filter(receipe_name__icontains = request.GET.get('search') )



    context = {'receipes': querySet}

    return render(request,'receipes.html',context)



def delete_receipe(request,id):
    receipe_id = id
    receipe = Receipe.objects.get(id=receipe_id)
    receipe.delete()
    return redirect('/receipes/')

def update_receipe(request,id):
    receipe_id = id
    receipe = Receipe.objects.get(id=receipe_id)

    if request.method=="POST":
        data = request.POST

        image = request.FILES.get('image')
        name = data.get('name', '')  # Set a default value for `name` in case it's not found
        description = data.get('description', '')  # Set a default value for `description`

        receipe.receipe_name = name
        receipe.receipe_description = description
        if image :
          receipe.receipe_image = image


        receipe.save();
        return redirect('/receipes/')
  

    context = {'receipe': receipe}


    return render(request,'update-receipes.html',context)

     