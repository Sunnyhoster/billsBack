import os
from django.http import HttpResponse

def showImage(fileName):
    d = os.path.dirname(__file__)
    imagePath = os.path.join(d, 'images/'+fileName+'.png')
    imageData = open(imagePath, 'rb').read()
    return HttpResponse(imageData, content_type='image/png')