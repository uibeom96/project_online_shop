from django import forms
from users.models import User

class SignupForm(forms.ModelForm):
    password = forms.CharField(label='패스워드', widget=forms.PasswordInput)
    password2 = forms.CharField(label='패스워드 확인', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("nick_name", "username", "password", "password2")

        labels = {
            "nick_name": "닉네임",
            "username": "아이디",
            }
    
    def clean_nick_name(self):
        check = self.cleaned_data.get("nick_name")
        if User.objects.filter(nick_name=check):
            raise forms.ValidationError("이미 존재하는 닉네임 입니다.") 
        return check

    def clean_password2(self):
        check = self.cleaned_data
        if check.get("password") != check.get("password2"):
            raise forms.ValidationError("패스워드가 서로 다릅니다.")
        return check.get("password2")