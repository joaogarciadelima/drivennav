from django import forms
from drivennav.data.models import Data


class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = "__all__"
