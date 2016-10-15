from django.test import TestCase
import uuid
from .models import Person


class ModelPersonTestCase(TestCase):
    def setUp(self):

        pass

    def test_create_person_requires_declarationstatusname(self):
        """A person object should not be saved if it doesn't have a valid DeclarationStatusName"""
        new_person = Person
        new_person.first_name = 'FirstName_ModelPersonTestCase_' + uuid.uuid4().__str__()
        new_person.last_name = 'LastName_ModelPersonTestCase_' + uuid.uuid4().__str__()
        with self.assertRaises(BaseException):
            new_person.save()
