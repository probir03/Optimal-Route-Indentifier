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
    
    def grid_by_id(self, grid_id, transform=False, transformer_name='transform'):
        '''Grid of a given id

        Args:
            grid_id: string(UUID)
            transform: boolean (option for tranforming data or not)
            transformer_name: str (transformer method name)
        
        Return:
            A dictionary of a grid
        '''
        query = {
            '_id': grid_id
        }
        filters = [
            {
                'is_deleted': {
                    '$ne': True
                }
            }
        ]
        grid = self.get_one(filters=filters, queries=query)
        
        if grid and transform:
            return getattr(self.transformer, transformer_name)(grid)
        return grid
    
    def update_grid_by_id(self, grid_id, grid, transform=False, transformer_name='transform'):
        '''Method to update grid in db by grid id

        Args:
            grid_id: string(UUID)
            grid: dictionary
            transform: boolean (option for tranforming data or not)
            transformer_name: str (transformer method name)
        
        Return:
            A dictionary of a grid
        '''
        current_epoch = helpers.current_epoch()
        grid['updated_at'] = current_epoch

        check_query = {
            '_id': {
                '$ne' : grid_id
            },
            'is_deleted': False,
            'name': grid.get('name')
        }

        if self.get_one(queries=check_query):
            return True, 'Grid name already exists'

        update_query = {
            '_id': grid_id,
            'is_deleted': False
        }

        data = {
            '$set': grid
        }

        grid = self.update_one(data, queries=update_query, return_document=True, upsert=True)
        
        if grid and transform:
            return False, getattr(self.transformer, transformer_name)(grid)
        return False, grid
    
    def delete_grid_by_id(self, grid_id):
        '''Method to delete a grid by id

        Args:
            grid_id: string(uuid)

        Return:
            either string or dict
        '''
        delete_data = {
            '$set' : {
                'is_deleted':  True
            }
        }
        query = {
            '_id': grid_id
        }
        res = self.update_one(delete_data, queries=query)
        if res:
            return False, res
        return True, "Cannot delete measure !"
