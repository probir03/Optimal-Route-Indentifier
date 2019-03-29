'''initializinf mongo connection'''
import pymongo
from pymodm import connect

from django.conf import global_settings, settings


MONGO_CRED = settings.DATABASE_SETTINGS['mongodb']

CLIENT = pymongo.MongoClient('mongodb://{userpass}{mongo_host}:{mongo_port}'.format(
    mongo_host=MONGO_CRED.get('HOST'),
    mongo_port=str(MONGO_CRED.get('PORT')),
    userpass='{username}{password}{at}'.format(
        username=MONGO_CRED.get('USER') or '',
        password=':' + MONGO_CRED['PASS'] if MONGO_CRED.get('PASS') else '',
        at='@' if MONGO_CRED.get('USER') else ''
    )))


def connect_dummy_db():
    '''creating dummy databse connection
    Args: None
    Retrun: None
    '''
    connect(
        'mongodb://{userpass}{mongo_host}:{mongo_port}/{db}'.format(
            mongo_host=MONGO_CRED.get('HOST'),
            mongo_port=str(MONGO_CRED.get('PORT')),
            db=MONGO_CRED.get('NAME'),
            userpass='{username}{password}{at}'.format(
                username=MONGO_CRED.get('USER') or '',
                password=':' + MONGO_CRED['PASS'] if MONGO_CRED.get('PASS') else '',
                at='@' if MONGO_CRED.get('USER') else ''
            )
        )
    )