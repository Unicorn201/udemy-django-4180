from django import forms
from .models import Post
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
# from .widgets import FileInputWithPreview

# from django.core.files.storage import default_storage


class  PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('thumbnail', 'title', 'category','content', )
  
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


class ContactForm(forms.Form):
    name = forms.CharField(
        label = '', 
        max_length = 100,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "お名前"
        })
    )
    email_address = forms.EmailField(
        label='',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': "メールアドレス",
        }),
    )
    inquiry = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': "お問い合わせ内容",
        }),
    )

    def send_email(self):
        # subject = "お問い合わせ"
        name = self.cleaned_data['name']
        email_address = self.cleaned_data['email_address']
        inquiry = self.cleaned_data['inquiry']
        from_email = '{name} <{email}>'.format(name = name, email = email_address)
        recipient_list = [settings.EMAIL_HOST_USER]  # 受信者リスト
        try:
            # send_mail(subject = name + "様からの問い合わせ", message = inquiry, from_email = from_email, recipient_list = recipient_list)
            message = EmailMessage(subject = name + "様からの問い合わせ", body = inquiry, from_email = from_email, to = recipient_list,)
                                    # cc = [from_email],
            #                     )
            message.send()

        except BadHeaderError:
            return HttpResponse("無効なヘッダが検出されました。")

    def clean_message(self):
        message = self.cleaned_data['message']
        if(message.find('<') != -1 or message.find('>') != -1):
            raise forms.ValidationError("恐れ入りますが問い合わせ内容でのタグ利用はお控えください。")
        return message