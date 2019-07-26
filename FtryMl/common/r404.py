from django.http import HttpResponse
from django.shortcuts import  redirect
 
def result(request):
    return HttpResponse('404!')

# 重定向到前端
def redirectIndex(request):
    return redirect('/ftryml-web')