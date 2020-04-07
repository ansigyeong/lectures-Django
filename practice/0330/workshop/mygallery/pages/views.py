from django.shortcuts import render
import requests

# Create your views here.

# https://api.unsplash.com/search/photos?client_id=aWAByM7N8JQXPXYgEBlgw9Gu11ssS_NMiq1GJJ4BMt4&query=person&color=yellow
def index(request):
    return render(request, 'index.html')

def gallery(request):
    #1. Access key 붙여놓기
    client_id = 'aWAByM7N8JQXPXYgEBlgw9Gu11ssS_NMiq1GJJ4BMt4'

    #2. 전송한 form 데이터 받아오기
    # reuqeust.GET -> dictionary like
    search_data = request.GET.get('search')

    #3. unsplash 서버로 요청 보내기
    photo_url = f'https://api.unsplash.com/search/photos?client_id={client_id}&query={search_data}&color=yellow'

    #4. 요청 -> 응답(json) -> 변환(dict)
    response = requests.get(photo_url).json()
    # print(response)

    #5. 사진 url을 넣을 리스트를 준비하기
    photo_list = []

    #6. 응답 데이터(리스트)를 순회하며 regular 사이즈의 이미지를 photo_list에 담기
    for photo in response.get('result'):
        photo_list.append(photo.get('urls').get('regular'))
    context = {
        'photo_list': photo_list,
    }
    return render(request, 'gallery.html', context)