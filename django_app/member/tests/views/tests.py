from django.test import TestCase
from django.urls import resolve
from django.urls import reverse

from member import views


class LoginViewTest(TestCase):
    VIEW_URL = '/member/login/'
    VIEW_URL_NAME = 'member:login'

    def test_url_equal_reverse_url_name(self):
        #주어진 VIEW_URL과 VIEW_URL_NAMEf reverse()한 결과가 같은지 검사
        self.assertEqual(self.VIEW_URL, reverse(self.VIEW_URL_NAME))

    def test_url_resolves_to_login_views(self):
        # login view 가 특정 url을 사용하고 있는지
        # resolve 함수를 이용해 특정 url이 참조하는 view를 검색
        found = resolve(self.VIEW_URL)
        self.assertEqual(found.func, views.login)

    def test_uses_login_template(self):
        # login view가 member/login.html을 사용하고 있는
        url = reverse(self.VIEW_URL_NAME)
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'member/login.html')