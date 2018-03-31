from django import forms
from django.forms import fields,widgets
from platformproject.models import *
from django.core.exceptions import ValidationError
import re

class UserInfo(forms.ModelForm):
    user_name = fields.CharField(
                                 min_length=6,
                                 max_length=12,
                                 strip=True,
                                 required=True,
                                 widget=widgets.TextInput(attrs={'placeholder': '用户名为8-12个字符'}),
                                 error_messages={
                                     'required': '用户名不能为空',
                                     'min_length': '用户名最少为6个字符',
                                     'max_length': '用户名最不超过为20个字符'
                                 }
                                 )
    user_hashpas = fields.CharField(
                                    required=True,
                                    widget=widgets.PasswordInput(attrs={'placeholder': '请输入密码，必须包含数字,字母,特殊字符'}),
                                    min_length=6,
                                    max_length=12,
                                    error_messages={
                                        'required': '密码不能为空',
                                        'min_length': '密码最少6个字符',
                                        'max_length': '密码不超过12个字符'
                                    }
                                    )
    pwd_again = fields.CharField(

        widget=widgets.PasswordInput(attrs={ 'placeholder': '请再次输入密码!'}),
        required=True,
        error_messages={'required': '请再次输入密码!!!!'}
    )
    #user_key = fields.CharField('识别码', max_length=32)
    user_email = fields.EmailField(
                                   widget=widgets.TextInput(attrs={'placeholder': '请输入邮箱'}),
                                    required = True,
                                    error_messages = {'required': '邮箱不能为空',
                                                    'invalid': '请输入正确的邮箱格式'}
                                    )

    def clean_user_name(self):
        username = self.cleaned_data.get('user_name')
        users = user.objects.filter(user_name=username).count()
        print(users)
        if users:
            raise ValidationError('用户名重复')
        return username

    def clean_user_email(self):
        email = self.cleaned_data.get('user_email')
        mobile_re = re.compile(r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$')
        if not mobile_re.match(str(email)):
            raise ValidationError('邮箱格式错误')
        return email

    def clean(self):
        password1 = self.cleaned_data.get('user_hashpas')
        password2 = self.cleaned_data.get('pwd_again')
        if password1 and password2 and password1 != password2:
            self.add_error('pwd_again','两次输入密码不一致')
            return None
        else:
            return self.cleaned_data

