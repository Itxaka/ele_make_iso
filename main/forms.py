from django import forms
from main.models import Jobs


class NewJob(forms.ModelForm):
    class Meta:
        model = Jobs
        fields = ["name", "yaml"]
        widgets = {
            "yaml": forms.Textarea(attrs={"cols": "120", "rows": "40"})
        }