from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import render, redirect


def login(request):
    # member/login.html 생성
    #   username, password button이 있는 HTML생성
    #   POST요청이 올 경우 좌측 코드를 기반으로 로그인 완료후 post_list로 이동
    #   실패할경우 HttpResponse로 'Login invalid!' 띄워주기
    if request.method == 'POST':
        pass
    else:
        return render(request, 'member/login.html')
