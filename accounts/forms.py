# -*- coding:utf-8 -*-
from django import forms
from .models import MyUser
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=50)
    email = forms.EmailField(label='邮箱')
    password1 = forms.CharField(label='密码', widget=forms.PasswordInput)
    password2 = forms.CharField(label='确认密码', widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if len(password1) < 6:
            raise forms.ValidationError("密码长度太短。")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("密码不能为空且必须相等。")
        return password2

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            MyUser.objects.get(username=username)
            raise forms.ValidationError("此用户名已使用。")
        except MyUser.DoesNotExist:
            return username


    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            MyUser.objects.get(email=email)
            raise forms.ValidationError("邮箱已注册。")
        except MyUser.DoesNotExist:
            return email



class LoginForm(forms.Form):
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='密码', widget=forms.PasswordInput)









class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('email', 'username', 'password', 'is_active', 'is_admin', 'is_member')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]