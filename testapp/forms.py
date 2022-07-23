from dataclasses import fields
from xml.dom import ValidationErr
from django.forms import ModelForm, ValidationError
from testapp.models import Student

class StudentForm(ModelForm):
    def clean_marks(self):
        input_marks=self.cleaned_data.get('marks')
        if input_marks < 35:
            raise ValidationError('Marks should be greater than 35 for passing')
        return input_marks
    class Meta:
        model=Student
        fields='__all__'