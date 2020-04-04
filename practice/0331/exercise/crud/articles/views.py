from django.shortcuts import render

# Create your views here.
def ping(request):
    return render(request, 'articlesping.html')

def pong(request):
    ping_data = request.GET.get('ping')
    context = {
        'ping_data': ping_data,
    }
    return render(request, 'articles/pong.html', context)