import pickle

from django import forms
from django.conf import settings

house_price_categories = pickle.load(open(f'{settings.BASE_DIR}/models/house_price_feature_categories.sav', 'rb'))
rent_categories = pickle.load(open(f'{settings.BASE_DIR}/models/rent_feature_categories.sav', 'rb'))


def choices_from_array(array):
    return [(x, x) for x in array]


class ApartmentInfoForm(forms.Form):
    price = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={
            'type': 'number',
            'class': 'form-control',
        }),
        initial=100000,
    )
    district = forms.ChoiceField(
        required=True,
        choices=choices_from_array(house_price_categories['district']),
        widget=forms.Select(attrs={
            'type': 'text',
            'class': 'form-select'
        })
    )
    neighborhood = forms.ChoiceField(
        required=True,
        choices=choices_from_array(house_price_categories['neighborhood']),
        widget=forms.Select(attrs={
            'type': 'text',
            'class': 'form-select'
        })
    )
    condition = forms.ChoiceField(
        required=True,
        choices=choices_from_array(house_price_categories['condition']),
        widget=forms.Select(attrs={
            'type': 'text',
            'class': 'form-select'
        })
    )
    type = forms.ChoiceField(
        required=True,
        choices=choices_from_array(house_price_categories['type']),
        widget=forms.Select(attrs={
            'type': 'text',
            'class': 'form-select'
        })
    )
    room_type = forms.ChoiceField(
        required=True,
        choices=choices_from_array(rent_categories['room_type']),
        widget=forms.Select(attrs={
            'type': 'text',
            'class': 'form-select'
        })
    )
    rooms = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={
            'type': 'number',
            'class': 'form-control',
        }),
        initial=1,
    )
    area_m2 = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={
            'type': 'number',
            'class': 'form-control',
        }),
        initial=30,
    )
    accommodates = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={
            'type': 'number',
            'class': 'form-control',
        }),
        initial=2,
    )
    lift = forms.ChoiceField(
        required=True,
        choices=choices_from_array(house_price_categories['lift']),
        widget=forms.Select(attrs={
            'type': 'text',
            'class': 'form-select'
        })
    )
    views = forms.ChoiceField(
        required=True,
        choices=choices_from_array(house_price_categories['views']),
        widget=forms.Select(attrs={
            'type': 'text',
            'class': 'form-select'
        })
    )
    floor = forms.ChoiceField(
        required=True,
        choices=choices_from_array(house_price_categories['floor']),
        widget=forms.Select(attrs={
            'type': 'text',
            'class': 'form-select'
        })
    )

    interest_rate = forms.FloatField(
        required=True,
        widget=forms.TextInput(attrs={
            'type': 'float',
            'class': 'form-control',
        })
    )

    loan_size = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={
            'type': 'number',
            'class': 'form-control',
        })
    )