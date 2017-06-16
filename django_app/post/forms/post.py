from django import forms

from ..models import Post


class PostForm(forms.ModelForm):
    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].required = True

    comment = forms.CharField(
        required=False,
        widget=forms.TextInput,
    )

    class Meta:
        model = Post
        fields = (
            'photo',
        )
