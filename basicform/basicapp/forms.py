from django import forms
from django.core import validators

class FormName(forms.Form):

    def check_for_capital(value):
        if (not value[0].isupper()):
            raise forms.ValidationError("Capital letter please")

    name = forms.CharField(validators=[check_for_capital,validators.MaxLengthValidator(4)])
    email = forms.EmailField()
    email_verify = forms.EmailField()
    text = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput)


    def clean_botcatcher(self):
        bot = self.cleaned_data['botcatcher']
        if (len(bot) > 0):
            raise forms.ValidationError("Gotcha bot")
        return bot

    def clean_email_verify(self):
        email = self.cleaned_data['email']
        v_email = self.cleaned_data['email_verify']

        if (email != v_email):
            raise forms.ValidationError("email doesnt match")

    def clean(self):
        all_clean = super().clean()
        return
