from django.shortcuts import HttpResponse, redirect # add redirect to import statement
from django.http import JsonResponse

def root_method(request):
    return redirect("/index")

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")


def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")


def create(request):
    return redirect("/")

def show(request,num):
    return HttpResponse("placeholder to display blog number "+str(num))

def edit(request,num):
    return HttpResponse("placeholder to edit blog "+str(num))


def destroy(request,num):
    return redirect("/blogs")



# def json_response(request):
#     return JsonResponse({
#         "response": "<span style='color:blue;'>JSON response from redirected_method</span>",
#         "status": True
#     }, safe=False)

    
