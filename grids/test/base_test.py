'''initial setup for test'''
from django.test import TestCase

from . import CLIENT
from . import MONGO_CRED
from . import connect_dummy_db


class BaseTest(TestCase):
    """docstring for BaseTest"""

    @classmethod
    def setUpClass(self):
        '''Method for test setup
        This method is called when test started
        '''
        connect_dummy_db()

    @classmethod
    def tearDownClass(cls):
        '''Methode to tear down the test setup
        This method is called on the completion of tests in this class
        '''
        CLIENT.drop_database(MONGO_CRED.get('NAME'))
