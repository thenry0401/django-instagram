from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class SignupForm(forms.Form):
    # SignupForm을 구성하고 해당 form을 view에서 사용하도록 설정
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

    username = forms.CharField(
        widget=forms.TextInput
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'Username already exist'
            )
        return username
