from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Tài Khoản', max_length=30)
    email = forms.CharField(label='Email')
    password1 = forms.CharField(label='Mật Khẩu', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Nhập lại mật khẩu', widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Mật khẩu không hợp lệ")