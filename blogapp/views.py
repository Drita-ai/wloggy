from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

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
        return HttpResponseNotFound("The blog title you entered is not yet created so redirecting to the first blog")
        