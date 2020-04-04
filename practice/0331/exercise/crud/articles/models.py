from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=140)
    content = models.TextField()

    # 제목 -> string
    # 내용 -> string
    # 나이 -> integer
    # age = models.IntegerField()

    # 글 생성 시각
    created_at = models.DateTimeField(auto_now_add=True)
    # 글 수정 시각
    updated_at = models.DateTimeField(auto_now=True)

    # migration 3단계
    # 1. python manage.py makemigrations -> 설계도 작성(db 반영 X)
    # 2. python manage.py showmigrations -> db 반영 여부 확인 (x 표시 여부)
    # 3. python manage.py migrate -> 실제 db에 반영하는 단계