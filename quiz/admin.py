# 관리자 모드에서 퀴즈 모델을 관리해줌

from django.contrib import admin
from .models import Quiz

admin.site.register(Quiz) # 관리자 페이지에서 퀴즈 모델 관리 가능