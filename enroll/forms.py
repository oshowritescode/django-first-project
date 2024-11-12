from django import forms

class studentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        if len(valname) < 4:
            raise forms.ValidationError("more than 4 rakh characters")
        valemail = self.cleaned_data['email']
        if len(valemail) < 10 :
            raise forms.ValidationError("more than 10 charcaters mai aana chahiye email tera bhai")