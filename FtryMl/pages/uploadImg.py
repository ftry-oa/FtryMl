from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import json
from .forms import UploadFileForm
from .img2Txt import img2Txt
from .kNN import writingKNN


def handle_uploaded_file(f):
    with open('temp/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return f.name, 'temp/'

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            imgName, imgPath = handle_uploaded_file(request.FILES['image'])
            context = {}
            if imgName and imgPath:
                txtPath = img2Txt(imgName, imgPath)
                result = writingKNN.handleWriting(txtPath)
                context['result'] = result
            return render(request, 'upload.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def uploadFileJson(request):
    context = {}
    print('upload file json', request.method)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            imgName, imgPath = handle_uploaded_file(request.FILES['image'])
            if imgName and imgPath:
                txtPath = img2Txt(imgName, imgPath)
                result = writingKNN.handleWriting(txtPath)
                context['data'] = result
                context['success'] = True
                return HttpResponse(json.dumps(context))
    context['success'] = False
    return HttpResponse(json.dumps(context))
