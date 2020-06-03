from django import forms
from drivennav.assumptions.models import Assumptions


class AssumptionsForm(forms.ModelForm):
    class Meta:
        model = Assumptions
        fields = "__all__"
