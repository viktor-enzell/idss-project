from django import forms


class ApartmentInfoForm(forms.Form):
    price = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={
            'type': 'number',
            'class': 'form-control',
            'placeholder': 'Enter price...'
        })
    )

    area = forms.ChoiceField(
        required=True,
        choices=(('gracia', 'Gracia'), ('eixample', 'Eixample'),),
        widget=forms.Select(attrs={
            'type': 'text',
            'class': 'form-select'
        })
    )
