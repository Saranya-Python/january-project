from django.test import TestCase


class TestMyUrls(TestCase):
    def test_home_url(self):
        response=self.client.get('/yup/home')
        self.assertEqual(response.status_code,200)