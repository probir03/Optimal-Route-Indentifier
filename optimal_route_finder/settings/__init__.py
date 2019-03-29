import select
import sys
from pymodm import connect
from django.conf import global_settings, settings

mongo_credentials = settings.DATABASE_SETTINGS['mongodb']

connect(
    'mongodb://{userpass}{mongo_host}:{mongo_port}/{db}'.format(
        mongo_host=mongo_credentials.get('HOST'),
        mongo_port=str(mongo_credentials.get('PORT')),
        db=mongo_credentials.get('NAME'),
        userpass='{username}{password}{at}'.format(
            username=mongo_credentials.get('USER') or '',
            password=':' +
            mongo_credentials['PASS'] if mongo_credentials.get('PASS') else '',
            at='@' if mongo_credentials.get('USER') else ''
        )
    )
)
