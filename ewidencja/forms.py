from django import forms
from ewidencja.models import Person
from ewidencja.widgets import NobodyExpectsSelect

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        widgets = {
            'city': NobodyExpectsSelect(),
        }