from django.shortcuts import render


def index(request):
    """
    Handling all GET and POST requests.
    """
    if request.method == 'GET':
        context = {
            'lorem_ipsum': f'Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                           f'Vivamus finibus lacus vel arcu cursus, nec elementum lectus '
                           f'posuere. Duis imperdiet libero vel dolor congue, eget luctus '
                           f'eros viverra. Morbi blandit posuere lacus, vel volutpat dui.',
        }
        return render(request, 'index.html', context)
