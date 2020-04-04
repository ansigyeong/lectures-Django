from django.shortcuts import render

# Create your views here.

def lotto(request):
    import random
    numbers = range(1, 46)
    lotto = random.sample(numbers, 6)
    context = {
        'lotto' : lotto,
    }
    return render(request, 'lotto.html', context)