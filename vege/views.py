from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth  import authenticate , login  , logout 
from django.contrib.auth.decorators  import login_required
# Create your views here.


@login_required(login_url='/login_page')
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

     

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username).first()

        if not user:  # If user does not exist
            messages.error(request, "Username does not exist.")
            return render(request, 'login.html')

        

        user = authenticate(request, username=username, password=password)
        
        if user is None:
            messages.error(request, "Invalid Password")
            return render(request, 'login.html')
        
        else:
            login(request,user)
            return redirect('/receipes/')



    return render(request,'login.html')







def register_page(request):
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register_page.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'register_page.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return render(request, 'register_page.html')
        

        user = User.objects.create (
            first_name = first_name,
            last_name = last_name,
            username = username,
            email = email,
        )

        user.set_password(password)  # Hash the password
        user.save()

        messages.success(request, "Registration successful. You can now log in.")
        return redirect('/login_page') 
    return render(request,'register_page.html')



def logout_page(request):
    logout(request)
    return redirect('/login_page')
