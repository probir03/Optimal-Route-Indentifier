'''Common heleper file'''

import uuid
from datetime import datetime


def current_epoch():
    '''returns current time while updating measures or value-set.

    Args:
        None

    Return:
        Integer
    '''
    cur_timestamp = datetime.now()
    return str(int(cur_timestamp.strftime("%s")) * 1000 +
               int(cur_timestamp.microsecond / 1000))


def generate_uuid():
    '''generting a unique uuid

    Args:
        None

    Return:
        String
    '''
    return str(uuid.uuid4())

def snake_to_camel_helper(val=None):
    '''
    helper function for snake_to_camel transformer

    Args:
        val(List)

    Return:
        val(List)
    '''
    for item in val:
        for item_key, item_val in item.items():
            new_key_name = convert_snake_to_camel(item_key)
            item[new_key_name] = item.pop(item_key, None)
    return val


def convert_snake_to_camel(item_key=None):
    '''
    convert snake case string to camel case string.

    Args:
        String

    Returns:
        String
    '''
    tmp = item_key.split('_')
    new_key_name = ''
    if(len(tmp) > 1):
        for cnt, split_val in enumerate(tmp):
            if cnt:
                new_key_name = new_key_name + f"{str(split_val).title()}"
            else:
                new_key_name = new_key_name + str(split_val)
        return new_key_name
    return item_key
