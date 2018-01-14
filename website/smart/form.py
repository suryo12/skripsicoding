from bootstrap_datepicker.widgets import DatePicker
from django import forms

class ToDoForm(forms.Form):
    todo = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    date = forms.DateField(widget=DatePicker(options={"format": "YYYY-MM-DD"}, fontawesome=True))