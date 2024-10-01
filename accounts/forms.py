from django import form
from .models import MyUser
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email','phone_number','full_number')

    def clean_password2(self):  #if user password1 will occure error cause password2 not producing at this time    
        cd = self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2']:
            raise ValidationError('passwords dont match')
        return cd['password2'] 

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
               user.save()
        return user       
        

 
class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text="you can change password using <a href=\"../password/\"> this form</a>")
                                                # \" yourtext \" - \" for escape to be without any meaning
                                                # one step go back then go to password

    class Meta:
        model = MyUser
        fields = ('email','phone_number','full_name','password','last_login')
