from django.test import TestCase, Client
from django.urls import reverse
from ..models import User


class LoginViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test', password='12345')

        self.client = Client()

    def tearDown(self):
        # Limpe dados ou configurações criadas no setUp()
        self.user.delete()

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertTemplateUsed(response, 'login.html')

    def test_login_view_post(self):
        response = self.client.post(reverse('login'), {
                                    'username': 'test', 'password': '12345'}, content_type="application/x-www-from-urlencoded")
        self.assertEqual(response.status_code, 302)

    def test_login_view_post_fail(self):
        response = self.client.post(reverse('login'), {
                                    'username': 'XXXX', 'password': '123456'}, content_type="application/x-www-from-urlencoded")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/auth/login', status_code=302,
                             target_status_code=301, fetch_redirect_response=True)

    def test_logout_view(self):
        response = self.client.get('/auth/sair/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/auth/login/', status_code=302,
                             target_status_code=200, fetch_redirect_response=True)
        


    def test_cadastro_view(self):
        response = self.client.get(reverse('cadastro'))
        self.assertTemplateUsed(response, 'cadastro.html')

    def test_cadastro_view_post(self):
        response = self.client.post(reverse('cadastro'), {
                                    'username': 'XXXX', 'password': '12345','check_password':'12345'}, content_type="application/x-www-from-urlencoded")
        self.assertEqual(response.status_code, 302)
        # self.assertRedirects(response, '/auth/login/', status_code=302, target_status_code=200, fetch_redirect_response=True)

    def test_cadastro_view_post_fail(self):
        response = self.client.post(reverse('cadastro'), {
                                    'username': 'XXXX', 'password': '12345','check_password':'123456'}, content_type="application/x-www-from-urlencoded")
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/auth/cadastro/', status_code=302,
                             target_status_code=200, fetch_redirect_response=True)
        