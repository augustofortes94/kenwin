from .test_setup import UserTestCase
from rest_framework import status
from ..models import Contact


class ContactTestCase(UserTestCase):
    def create_contact(self):
        return Contact.objects.create(
                                    firstname='firstnametest',
                                    lastname='lastnametest',
                                    enterprice='enterpricetest',
                                    number=1234567,
                                    email='test@test.com',
                                    address='addresstest',
                                )

    def test_get_contact(self):
        contact = self.create_contact()
        response = self.client.get('/api/contacts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['contacts'][0]['id'], contact.id)
        self.assertEqual(response.data['contacts'][0]['firstname'], contact.firstname)
        self.assertEqual(response.data['contacts'][0]['lastname'], contact.lastname)
        self.assertEqual(response.data['contacts'][0]['enterprice'], contact.enterprice)
        self.assertEqual(response.data['contacts'][0]['number'], str(contact.number))
        self.assertEqual(response.data['contacts'][0]['email'], contact.email)
        self.assertEqual(response.data['contacts'][0]['address'], contact.address)

    def test_post_contact(self):
        response = self.client.post('/api/contacts/',
                                    {'firstname': 'firstnametest',
                                        'lastname': 'lastnametest',
                                        'enterprice': 'enterpricetest',
                                        'number': 1234567,
                                        'email': 'test@test.com',
                                        'address': 'addresstest'}
                                    )
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
