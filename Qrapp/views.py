from django.shortcuts import render
from Qrapp.forms import QRForm
import qrcode
import os 
from django.conf import settings
# Create your views here.
def Qr_generator(request):
    if request.method=='POST':
          form =QRForm(request.POST)
          if form.is_valid():
              name=form.cleaned_data['Name']
              url=form.cleaned_data['url']

              #generate qrcode
              qr=qrcode.make(url)
              file_name=name +'.png'
              file_path=os.path.join(settings.MEDIA_ROOT,file_name)
              qr.save(file_path)
              #create image url
              qr_url=os.path.join(settings.MEDIA_URL,file_name)
              return render(request, 'qr_result.html',{'name':name,'qr_url':qr_url,'file_name':file_name})
    else:
       form =QRForm()

       return render(request, 'Qr_generator.html',{'form':form})