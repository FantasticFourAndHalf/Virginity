# By Zhufyak V.V
# zhufyakvv@gmail.com
# github.com/zhufyakvv
# 26.09.2017
from django import forms


class PhoneForm(forms.Form):
    phone = forms.CharField(label='Phone number')
    phone.widget = forms.NumberInput(attrs={'class': 'mdl-textfield__input'})

    def clean(self):
        cleaned_data = super(PhoneForm, self).clean()
        phone = cleaned_data.get("phone")

        if len(phone) == 9:
            raise forms.ValidationError(
                "Password and Confirm Password does not match."
            )
