from django import forms

class NewUrlEntryForm(forms.Form):
    url = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'URL goes here'}))

class NewUrlBookmarkedForm(forms.Form):
    url = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'URL goes here'}))