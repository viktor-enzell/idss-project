from django.shortcuts import render

from project.forms import ApartmentInfoForm


def index(request):
    """
    Handling all GET and POST requests.
    """
    if request.method == 'GET':
        if request.GET.get('price', False):
            apartment_info_form = ApartmentInfoForm(request.GET)
            if apartment_info_form.is_valid():
                price = apartment_info_form.cleaned_data.get('price', False)
                request.session['price'] = price

                area = apartment_info_form.cleaned_data.get('area', False)
                request.session['area'] = area

                context = {
                    'apartment_info_form': apartment_info_form,
                    'price': price,
                    'area': area,
                }
                return render(request, 'index.html', context)

        apartment_info_form = ApartmentInfoForm()
        context = {
            'apartment_info_form': apartment_info_form,
        }
        return render(request, 'index.html', context)
