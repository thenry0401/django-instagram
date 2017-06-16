from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': '사용자 아이디를 입력하세요'
            }
        )
    )
    password = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '비밀번호를 입력하세요'
            }
        )
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        user = authenticate(
            username=username,
            password=password
        )
        if user is not None:
            self.cleaned_data['user'] = user
        else:
            raise forms.ValidationError(
                'Login credentials not valid'
            )
        return self.cleaned_data