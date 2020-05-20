from django import forms


class DownloadForm(forms.Form):
    url = forms.CharField(label=' url', max_length=100)
