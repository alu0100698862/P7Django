from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
 
# Create your views here.

#def quick_test(request):
#	return HttpResponse("Hello testing world!");

def quick_test(request):
	return render_to_response("blog.html", {})

def test1(request):
    return render_to_response("blog1.html", {})
    
def test2(request):
    return render_to_response("blog2.html", {})
    
def test3(request):
    return render_to_response("blog3.html", {})
