from django import forms
from .models import Post
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
# from django.core.files.storage import default_storage


class  PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category','content', 'thumbnail')

    def __init__(self, *args, **kyargs):
        super().__init__(*args, **kyargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
    """
    def save(self):
        upload_file = self.files['file']
        file_name = default_storage.save(upload_file.name, upload_file)
        return default_storage.url(file_name)
    """

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kyargs):
        super().__init__(*args, **kyargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')
        
    def __init__(self, *args, **kyargs):
        super().__init__(*args, **kyargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class SearchForm(forms.Form):
    freeword = forms.CharField(min_length=1, max_length=30, label='', required=False)

    def __init__(self, *args,**kyargs):
        super().__init__(*args,**kyargs)