from django import forms
from django_recaptcha.fields import ReCaptchaField

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class solicitudForm(forms.Form):
    tipo_solicitud_opciones=[
        ("Proyecto","Proyecto"),
        ("Queja","Queja"),
        ("Sugeriencia","Sugeriencia")
    ]
    tipo_solicitud = forms.CharField(widget=forms.Select(choices=tipo_solicitud_opciones, attrs={
        "class" : "form-select"
    }))
    titulo_solicitud = forms.CharField()
    descripcion_solicitud = forms.CharField(widget=forms.Textarea)
    objetivo_solicitud = forms.CharField(widget=forms.Textarea)
    archivo_solicitud = forms.FileField()
    reCaptcha_solicitud = ReCaptchaField()


class solicitud_Empleo_Form(forms.Form):
    archivo_curriculum = forms.FileField()
    id_empleo = forms.CharField()

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Usuario
#         fields = ['avatar']