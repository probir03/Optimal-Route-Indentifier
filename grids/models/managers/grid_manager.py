''' pymodm manager for Grids Collection'''

from commons.utils.default_model_manager import DefaultManager
from commons.utils import helpers
from grids.models.transformers.grid_transformer import GridTransformer

class GridManager(DefaultManager):
    '''Grid manager for intracting to MonogDB'''

    def __init__(self):
        '''initializing requierd object'''
        self.transformer = GridTransformer()

    def search_by_name(self, name):
        '''serach grid by name
        
        Args:
            name: str
        
        Return:
            boolean
        '''
        query = {
            'name': name,
            'is_deleted': False
        }
        grid = self.get_one(queries=query)
        if grid:
            return True
        return False

    def add_grid(self, data, transform=False, transformer_name='transform'):
        '''create a new measure with provided data

        Args:
            data: dictionary 
            transform: boolean (option for tranforming data or not)

        Returns:
            Dictionary of the created document
        '''
        current_epoch = helpers.current_epoch()
        data['_id'] = helpers.generate_uuid()
        data['updated_at'] = current_epoch
        data['created_at'] = current_epoch

        new_grid = self.insert_one(data)
        if transform:
            return getattr(self.transformer, transformer_name)(new_grid)
        return new_grid

    def grid_list(self, query_obj=None, projection=None, limit=None, offset=None,
                  transform=False, transformer_name='transform'):
        '''Lists all model documents matching method args

        Queries on a specific collection and gets documents according to method args.

        Args:
            limit: integer limit for pagination.
            offset: integer offset for pagination
            transform: boolean (option for tranforming data or not)
            transformer_name: str (transformer method name)

        Returns:
            A list of model dictionaries matching the query.
        '''
        filters = [
            {'is_deleted': {'$ne': True}}
        ]
        grids, count, new_offset = self.get_paginated(filters=filters,
                                                      limit=limit, offset=offset)

        if transform:
            return getattr(self.transformer, transformer_name)(grids), count, new_offset
        return grids, count, new_offset