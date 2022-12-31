from django import forms
from .models import Commission


class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email': 'Email',
            'details': 'Enter your request here and we will get back to you as soon as possible',
        }
