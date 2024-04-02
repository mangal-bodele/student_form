from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"

        labels = {
            'fn':'First Name',
            'ln':'Last Name',
        }
        widgets = {
            'roll': forms.NumberInput(attrs={'class':'form-control'}),
            'fn': forms.TextInput(attrs={'class':'form-control'}),
            'ln': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.Textarea(attrs={'class':'form-control','rows':3}),
            'institute': forms.TextInput(attrs={'class':'form-control'}),
            'blood_group': forms.Select(attrs={'class':'form-control'}),
            'gender': forms.Select(attrs={'class':'form-control'})
        }