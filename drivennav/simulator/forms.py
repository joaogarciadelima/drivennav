from django import forms
from drivennav.simulator.models import Simulator


class SimulatorForm(forms.ModelForm):
    class Meta:
        model = Simulator
        fields = "__all__"
