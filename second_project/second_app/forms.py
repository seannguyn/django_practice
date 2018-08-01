from django import forms
from django.core import validators
from second_app.models import User

class FormName(forms.Form):

    form_name = forms.CharField()
    form_email = forms.EmailField()
    form_email_verify = forms.EmailField()
    form_password = forms.CharField(max_length=10)
    form_password_verify = forms.CharField(max_length=10)

    def clean_email_verify(self):
        email = self.cleaned_data['form_email']
        email_verify = self.cleaned_data['form_email_verify']

        if (email != email_verify):
            raise ValidationError("Email does not match")


    def clean_password_verify(self):
        password = self.cleaned_data['form_password']
        password_verify = self.cleaned_data['form_password_verify']

        if (email != email_verify):
            raise ValidationError("Password does not match")

class UserForm(forms.ModelForm):

    form_email_verify = forms.EmailField()
    password = forms.CharField(max_length=10,widget=forms.PasswordInput(attrs={'class':'form2'}))
    form_password_verify = forms.CharField(max_length=10,widget=forms.PasswordInput(attrs={'class':'form2'}), label='Retype password')
    field_order = ['name', 'email', 'form_email_verify','password','form_password_verify']

    class Meta:
        model = User
        fields = "__all__"

    def clean(self):
    #run the standard clean method first
            cleaned_data=super(UserForm, self).clean()
            password = cleaned_data.get("password")
            password_verify = cleaned_data.get("form_password_verify")
            email = cleaned_data.get("email")
            email_verify = cleaned_data.get("form_email_verify")

            #check if passwords are entered and match
            if password and password_verify and password==password_verify:
                print("pwd ok")
            else:
                raise forms.ValidationError("Passwords do not match!")

            if email and email_verify and email == email_verify:
                print("pwd ok")
            else:
                raise forms.ValidationError("Email do not match!")
            #always return the cleaned data
            return cleaned_data

    # def clean_email_verify(self):
    #     print("hello")
    #     email = self.cleaned_data['email']
    #     print(email = self.cleaned_data['email'])
    #     email_verify = self.cleaned_data['form_email_verify']
    #
    #     if (email != email_verify):
    #         raise ValidationError("Email does not match")
    #
    # def clean_password_verify(self):
    #     password = self.cleaned_data['password']
    #     password_verify = self.cleaned_data['form_password_verify']
    #
    #     if (email != email_verify):
    #         raise ValidationError("Password does not match")
