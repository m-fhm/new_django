from django import forms

class myform(forms.Form):
    name = forms.CharField(
        label='Enter Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class':'form-control'})
     )
    email =forms.EmailField(
        label='Enter Email',
         max_length=100,
         widget=forms.EmailInput(attrs={'class':'form-control'})
         )