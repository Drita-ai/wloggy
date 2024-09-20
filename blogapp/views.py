from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# TEMP-DB
blog_data={
    "blog1":"This is the best platform to render some contents",
    "blog2":"Will just keep this as simple as possible"
}

# Create your views here.
def index(request):
    return HttpResponse("Works")

def blog_display(request,blog):
    try:
        blog_content = blog_data[blog]
        return HttpResponse(blog_content)
    except:
        redirect_path = reverse("blog-url",args=["blog1"])
        print(redirect_path)
        return HttpResponseRedirect(redirect_path)
        