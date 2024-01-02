from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('fullname','mobile','index_number','department')
        labels = {
            'fullname':'Full Name',
            'index_number':'Index Number'
        }
    
    def __init__(self, *args, **kwargs):
        super(StudentForm,self).__init__(*args, **kwargs)
        self.fields['department'].empty_label = "Select"
        self.fields['index_number'].required = False