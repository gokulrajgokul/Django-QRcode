from django import forms

class QRForm(forms.Form):
    Name=forms.CharField (
        max_length=50 ,
        label='Name',
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'enter the QR Name'
        })
            )
    url=forms.URLField(
        max_length=230 ,
         label='URL',
         widget=forms.URLInput(attrs={
             'class':'form-control',
             'placeholder':'Enter the URL',
         }))