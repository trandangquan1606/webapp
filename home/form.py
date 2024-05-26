from django import forms
import re
from django.contrib.auth.models import User
class RegistrationForm(forms.Form):
    username = forms.CharField(label='Tài khoản')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError('Mật khẩu không khớp')

    def clean_username(self):
        username = self.cleaned_data['username']
    # Kiểm tra tên người dùng có ký tự đặc biệt hay không
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")
        # Kiểm tra tên người dùng đã tồn tại hay chưa
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")

    def save(self):
    # Tạo tài khoản người dùng
        User.objects.create_user(username=self.cleaned_data['username'],email=self.cleaned_data['email'],password=self.cleaned_data['password1'],)