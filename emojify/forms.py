from django import forms


class MsgInputForm(forms.Form):
    text = forms.CharField(initial='I love this site', required=False)

class MsgOutputForm(forms.Form):
    output = forms.CharField(required=False)