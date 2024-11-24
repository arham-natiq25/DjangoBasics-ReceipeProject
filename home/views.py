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
    return render(request,"Home/index.html")


def success_page(request):
    return HttpResponse("<h1>This is success page </h1>")