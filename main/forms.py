from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class solicitudForm(forms.Form):
    titulo = forms.CharField()
    descripcion = forms.CharField()

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Usuario
#         fields = ['avatar']