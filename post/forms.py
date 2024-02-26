from django import forms

from post.models import Post, Comment


class PostForm(forms.Form):
    title = forms.CharField(max_length=100, min_length=3)
    content = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField(required=False, label='Картинка')

    def clean_title(self):
        title = self.cleaned_data['title']
        if "python" in title.lower():
            # raise Exception("Python is not allowed")
            raise forms.ValidationError("Python is not allowed")

        return title.capitalize()
    
    def clean_content(self):
        content = self.cleaned_data['content']
        if "django" in content.lower():
            raise forms.ValidationError("Django is not allowed")

        return content

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if title and content:
            if title.lower() == content.lower():
                raise forms.ValidationError("Title and content must be different")
        
        return cleaned_data
    

class PostForm2(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['rate']
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control'}),
        # }
        labels = {
            'title': 'Заголовок',
            'content': 'Содержание',
            'image': 'Картинка'
        }
        help_texts = {
            'title': 'Some useful help text'
        }
        
    def clean_title(self):
        title = self.cleaned_data['title']
        if "python" in title.lower():
            # raise Exception("Python is not allowed")
            raise forms.ValidationError("Python is not allowed")

        return title.capitalize()
    
    def clean_content(self):
        content = self.cleaned_data['content']
        if "django" in content.lower():
            raise forms.ValidationError("Django is not allowed")

        return content

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')

        if title and content:
            if title.lower() == content.lower():
                raise forms.ValidationError("Title and content must be different")
        
        return cleaned_data
    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': 'Комментарий'
        }
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }
    