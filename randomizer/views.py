from django.shortcuts import render
from random import randint


def generate_number(request):
    return render(request, 'randomizer/num_generator.html')


def random_number(request):
    start_diapason = int(request.GET.get('first_number'))
    end_diapason = int(request.GET.get('second_number'))
    try:
        random_number = randint(start_diapason, end_diapason)
    except ValueError:
        return render(request, 'randomizer/num_generator.html', {'error': 'Please, enter a valid range!'})
    context = {
        'random_number': random_number,
        'start_diapason': start_diapason,
        'end_diapason': end_diapason
    }
    return render(request, 'randomizer/random_number.html', context)

