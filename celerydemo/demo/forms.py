from django import forms


class EmailForm(forms.Form):
    message = forms.CharField(required=True, widget=forms.Textarea)
    email = forms.EmailField(required=True)
