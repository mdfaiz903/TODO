from django import forms
from . models import todo_model

class todoForm(forms.ModelForm):
   class Meta:
        model = todo_model
        fields = ['title','description']

        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control'}),
                'description': forms.Textarea(attrs={'class': 'form-control','rows':2}),
                # Add more fields here if needed
            }


      
   

    