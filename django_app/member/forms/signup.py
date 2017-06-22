from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class SignupForm(forms.Form):
    # SignupForm을 구성하고 해당 form을 view에서 사용하도록 설정
<<<<<<< HEAD
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super().__init__(*args, **kwargs)

    username = forms.CharField(
        widget=forms.TextInput
    )
    nickname = forms.CharField(
        widget=forms.TextInput
=======
    username = forms.CharField(
        help_text='Signup help text test',
        widget=forms.TextInput
    )
    nickname = forms.CharField(
        widget=forms.TextInput,
        help_text='닉네임은 유일해야 합니다',
        max_length=24,
>>>>>>> e5278c3fc0369ff8fa911dace01b1d0a28cb1c8d
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput
    )

<<<<<<< HEAD
=======
    # clean_<fieldname>메서드를 사용해서
    # username필드에 대한 유효성 검증을 실행
>>>>>>> e5278c3fc0369ff8fa911dace01b1d0a28cb1c8d
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError(
<<<<<<< HEAD
                '이미 존재하는 아이디입니다'
=======
                'Username already exist'
>>>>>>> e5278c3fc0369ff8fa911dace01b1d0a28cb1c8d
            )
        return username

    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        if nickname and User.objects.filter(nickname=nickname).exists():
            raise forms.ValidationError(
<<<<<<< HEAD
                '이미 존재하는 닉네임입니다'
=======
                'Nickname already exist'
>>>>>>> e5278c3fc0369ff8fa911dace01b1d0a28cb1c8d
            )
        return nickname

    def clean_password2(self):
<<<<<<< HEAD
=======
        # password1과 password2를 비교하여 같은지 검증
        # password2필드에 clean_<fieldname>을 재정의한 이유는,
        #   cleaned_data에 password1이 이미 들어와 있어야 하기 때문
>>>>>>> e5278c3fc0369ff8fa911dace01b1d0a28cb1c8d
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
<<<<<<< HEAD
                '비밀번호가 다릅니다'
=======
                'Password mismatch',
>>>>>>> e5278c3fc0369ff8fa911dace01b1d0a28cb1c8d
            )
        return password2

    def create_user(self):
<<<<<<< HEAD
        username = self.cleaned_data['username']
        password2 = self.cleaned_data['password2']
        nickname = self.cleaned_data['nickname']
        return User.objects.create_user(
            username=username,
            password=password2,
            nickname=nickname,
        )

=======
        # 자신의 cleaned_data를 사용해서 유저를 생성
        # 생성한 유저를 반환
        username = self.cleaned_data['username']
        password = self.cleaned_data['password2']
        nickname = self.cleaned_data['nickname']
        return User.objects.create_user(
            username=username,
            nickname=nickname,
            password=password
        )
>>>>>>> e5278c3fc0369ff8fa911dace01b1d0a28cb1c8d
