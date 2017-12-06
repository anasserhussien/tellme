from django import forms
from django.contrib.auth.models import User
from .models import Profile, Message

class UserForm(forms.ModelForm):

    class Meta:
        Model = User
        fields = ('username','email','password')

class ProfileForm(forms.ModelForm):

    class Meta:
        Model = Profile
        fields = ('bio','date_of_birth')

class MessageForm(forms.ModelForm):
    from_user = forms.IntegerField(widget= forms.HiddenInput(), required = False)
    to_user = forms.IntegerField(widget= forms.HiddenInput(),required = False)
    date = forms.DateTimeField(widget = forms.HiddenInput(),required = False)
    content = forms.CharField(required = True, widget = forms.Textarea)

    class Meta:
        model = Message
        fields = ('from_user', 'to_user','date','content')
