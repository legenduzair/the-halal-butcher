from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'display_name',
                  'phone_number', 'street_address',
                  'town_or_city', 'county', 'postcode',
                  'country', 'email_address')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'display_name': 'Display Name',
            'phone_number': 'Phone Number',
            'town_or_city': 'Town or City',
            'street_address': 'Street Address',
            'county': 'County, State or Locality',
            'postcode': 'Postal Code',
            'email_address': 'Email Address',
        }

        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
