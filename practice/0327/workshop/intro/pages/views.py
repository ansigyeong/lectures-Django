from django.shortcuts import render

# Create your views here.

def dinner(request, menu, people):
  print(request)
  print(menu)
  print(people)
  context = {
    'menu': menu,
    'people': people,
  }
  return render(request, 'dinner.html', context)