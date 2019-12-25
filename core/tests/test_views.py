from django.test import TestCase


class ValuesViewTests(TestCase):

    def test_view_post_data(self):
        response = self.client.post('/values', {'age': 13, 'city': 'dhaka'})
        self.assertEqual(response.status_code, 201)

        self.assertJSONEqual(response.content.decode("utf-8"), {'message': 'Successfully stored'})

    def test_view_return_dict(self):
        self.client.post('/values', {'age': 13, 'city': 'dhaka'})
        response = self.client.get('/values')
        self.assertJSONEqual(response.content.decode("utf-8"), {'age': 13, 'city': 'dhaka'})

        response = self.client.get('/values', {'keys': 'age'})
        self.assertJSONEqual(response.content.decode("utf-8"), {'age': 13})

    def test_view_put_or_patch(self):
        self.client.post('/values', {'name': 'john', 'age': 23})

        response = self.client.put('/values', {'name': 'doe'})
        self.assertJSONEqual(response.content.decode("utf-8"), {'message': 'Successfully updated'})
