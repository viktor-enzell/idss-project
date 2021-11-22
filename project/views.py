from django.shortcuts import render

from project.forms import ApartmentInfoForm
from project.price_predictor import PricePredictor

price_predictor = PricePredictor()


def index(request):
    """
    Handling all GET and POST requests.
    """
    if request.method == 'GET':
        if request.GET.get('price', False):
            apartment_info_form = ApartmentInfoForm(request.GET)
            if apartment_info_form.is_valid():
                price = apartment_info_form.cleaned_data.get('price')
                district = apartment_info_form.cleaned_data.get('district')
                neighborhood = apartment_info_form.cleaned_data.get('neighborhood')
                condition = apartment_info_form.cleaned_data.get('condition')
                apt_type = apartment_info_form.cleaned_data.get('type')
                rooms = apartment_info_form.cleaned_data.get('rooms')
                area_m2 = apartment_info_form.cleaned_data.get('area_m2')
                lift = apartment_info_form.cleaned_data.get('lift')
                views = apartment_info_form.cleaned_data.get('views')
                floor = apartment_info_form.cleaned_data.get('floor')

                price_prediction = price_predictor.predict(
                    district, neighborhood, condition, apt_type, rooms,
                    area_m2, lift, views, floor
                )

                context = {
                    'apartment_info_form': apartment_info_form,
                    'price_prediction': price_prediction,
                }
                return render(request, 'index.html', context)

        apartment_info_form = ApartmentInfoForm()
        context = {
            'apartment_info_form': apartment_info_form,
        }
        return render(request, 'index.html', context)
