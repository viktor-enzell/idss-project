from django.shortcuts import render

from project.forms import ApartmentInfoForm
from project.price_predictor import PricePredictor
from project.rent_predictor import RentPredictor

price_predictor = PricePredictor()
rent_predictor = RentPredictor()


def index(request):
    """
    Handling all GET and POST requests.
    """
    if request.method == 'GET':
        if request.GET.get('price', False):
            apartment_info_form = ApartmentInfoForm(request.GET)
            if apartment_info_form.is_valid():
                # Price prediction features
                neighborhood = apartment_info_form.cleaned_data.get('neighborhood')
                condition = apartment_info_form.cleaned_data.get('condition')
                apt_type = apartment_info_form.cleaned_data.get('type')
                area_m2 = apartment_info_form.cleaned_data.get('area_m2')
                lift = apartment_info_form.cleaned_data.get('lift')
                views = apartment_info_form.cleaned_data.get('views')
                floor = apartment_info_form.cleaned_data.get('floor')

                # Rent prediction features
                room_type = apartment_info_form.cleaned_data.get('room_type')
                accommodates = apartment_info_form.cleaned_data.get('accommodates')

                # Shared features
                district = apartment_info_form.cleaned_data.get('district')
                rooms = apartment_info_form.cleaned_data.get('rooms')

                # Other features
                price = apartment_info_form.cleaned_data.get('price')

                price_prediction = price_predictor.predict(
                    district, neighborhood, condition, apt_type, rooms,
                    area_m2, lift, views, floor
                )
                rent_prediction = rent_predictor.predict(
                    room_type, district, accommodates, rooms
                )

                context = {
                    'prediction_made': True,
                    'apartment_info_form': apartment_info_form,
                    'price_prediction': price_prediction,
                    'rent_prediction': rent_prediction,
                    'actual_price': price,
                    'price_difference': price_prediction - price,
                }
                return render(request, 'index.html', context)

        apartment_info_form = ApartmentInfoForm()
        context = {
            'apartment_info_form': apartment_info_form,
        }
        return render(request, 'index.html', context)
