from new_app.models import school
from django import forms
class colform(forms.ModelForm):
    class Meta:
        model = school
        fields= '__all__'
