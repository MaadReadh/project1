from django import forms

class EntryCreatForm(forms.Form):
     title = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Title", "class": "form-control"}),  required=True)
     content = forms.CharField(widget=forms.Textarea(
        attrs={"placeholder": "Content", "rows": 12, "class": "form-control"}), required=True)


class EditEntry(forms.Form):
    title = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Title", "class": "form-control"}),  required=True)
    content = forms.CharField(widget=forms.Textarea(
        attrs={"placeholder": "Content", "rows": 12, "class": "form-control"}), required=True)
