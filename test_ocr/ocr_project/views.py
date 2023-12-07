from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import  ImageUploadForm
from .models import ImageUploadedForm
import pytesseract
from keras_ocr import pipeline


# Create your views here.
def index(request):
    return HttpResponse("hello")

# def image_request(request):  
#     if request.method == 'POST':  
#         form = UserImageForm(request.POST, request.FILES)  
#         if form.is_valid():  
#             form.save()  
  
#             # Getting the current instance object to display in the template  
#             img_object = form.instance  
              
#             return render(request, 'image_form.html', {'form': form, 'img_obj': img_object})  
#     else:  
#         form = UserImageForm()  
  
#     return render(request, 'image_form.html', {'form': form}) 
 
# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Success")
#         else:
#             form = UploadFileForm()
#         return render(request, "upload.html", {"form":form})

def uploaded_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            ocr_text = perform_ocr(instance.image.path)
            # print(ocr_text)
            return render(request, 'ocrresult.html', {'ocr_text':ocr_text})
    else:
        form = ImageUploadForm()
    return render(request, 'uploadimage.html', {'form':form})

def perform_ocr(image_path):
    # pytesseract.pytesseract.tesseract_cmd = r'/usr/share/tesseract-ocr/4.00/tessdata'
    pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
   # pytesseract.pytesseract.tesseract_cmd = r'/../'
    #tessdata_dir_config = r'--tessdata-dir "/usr/share/tesseract-ocr/4.00/tessdata"'
    #pytesseract.pytesseract.tesseract_cmd = r'/mnt/d/E/a_mrcet/sem_5/as1/project/'

    text_tesseract = pytesseract.image_to_string(image_path)
    pipeline1 = pipeline.Pipeline()
    images = [image_path]
    prediction_group = pipeline1.recognize(images)
    text_keras_ocr = ' '.join([results[0] for results in prediction_group[0]])

    combined_text = f"Pytesseract OCR: {text_tesseract}\n\ni  Keras OCR: {text_keras_ocr}"
    #combined_text = f"Pytesseract OCR: \n\nKeras OCR: {text_keras_ocr}"
    # print(combined_text)
    #return render(request, 'ocrresult.html', {'combined_text':combined_text})
    return combined_text



