from django import forms

from ..models import Post, Comment


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

    def save(self, **kwargs):
        # 전달된 키워드인수중 'commit'키 값을 가져옴
        commit = kwargs.get('commit', True)
        # 전달된 키워드인수중 'author'키 값을 가져오고 기본 kwargs dict에서 제외
        author = kwargs.pop('author', None)

        self.instance.author = author
        instance = super().save(**kwargs)

        comment_string = self.cleaned_data['comment']
        if commit and comment_string:
            instance.comment_set.create(
                author=instance.author,
                content=comment_string
            )
        return instance