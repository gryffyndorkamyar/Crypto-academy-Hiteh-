from django import forms
from django.contrib.auth.models import User
from post.models import Profile





class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'username']

class ComplaintForm(forms.Form):
    name = forms.CharField(max_length=100, label='نام')
    email = forms.EmailField(label='ایمیل')
    complaint = forms.CharField(widget=forms.Textarea, label='شکایت')