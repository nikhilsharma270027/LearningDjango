from django import forms
from .models import ChaiVarity

class ChaiVarietyForm(forms.Form):
  # This form allows users to select a chai variety from the available options.
  # The queryset is set to all ChaiVarity objects, allowing users to choose from the database.
  chai_variety = forms.ModelChoiceField(queryset=ChaiVarity.objects.all(), label="Select Chai Variety")