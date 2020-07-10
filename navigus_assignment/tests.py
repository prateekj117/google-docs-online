from django.test import TestCase


class BasicTest(TestCase):
    def test_base_url_return_correct_status_code(self):
        response = self.client.get('http://localhost:8000/')
        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_user_gets_redirected(self):
        response = self.client.get('http://localhost:8000/presence')
        self.assertEqual(response.status_code, 301)
