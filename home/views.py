from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# def home (request):
#     return HttpResponse ("""Hey I am Jango Server
#                             <br>
#                          <p>HELLO FROM P</p>
#                          <hr/>
#                          """)
def home (request):

    peoples = [
        {'name' : 'Arham',
         'age' : 20
        },
        {'name' : 'Saad',
         'age' : 16
        },
        {'name' : 'Subhan',
         'age' : 10
        },
    ]
    page = "Home"
    return render(request,"Home/index.html",context={"peoples":peoples,"page":page})


def success_page(request):
    return HttpResponse("<h1>This is success page </h1>")