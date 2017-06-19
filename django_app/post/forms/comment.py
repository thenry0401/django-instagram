from django import forms


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['photo'].required = True
        if self.instance.my_comment:
            self.fields['comment'].initial = self.instance.my_comment.content

    comment = forms.CharField(
        required=False,
        widget=forms.TextInput
    )

    class Meta:
        model = Post
        fields = (
            'photo',
            'comment',
        )

    def save(self, **kwargs):
        # 전달된 키워드인수중 'commit'키 값을 가져옴
        commit = kwargs.get('commit', True)
        # 전달된 키워드인수중 'author'키 값을 가져오고, 기존 kwargs dict에서 제외
        author = kwargs.pop('author', None)

        if not self.instance.pk or isinstance(author, User):
            self.instance.author = author

        instance = super().save(**kwargs)

        comment_string = self.cleaned_data['comment']
        if commit and comment_string:
            if instance.my_comment:
                instance.my_comment.content = comment_string
                instance.my_comment.save()
            else:
                instance.my_comment = Comment.objects.create(
                    post=instance,
                    author=instance.author,
                    content=comment_string
                )
            instance.save()
        return instance