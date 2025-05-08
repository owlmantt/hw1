# posts/tests.py
class PostTests(APITestCase):
    def test_create_post(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/posts/', {'title': 'Test', 'content': '...'})
        self.assertEqual(response.status_code, 201)