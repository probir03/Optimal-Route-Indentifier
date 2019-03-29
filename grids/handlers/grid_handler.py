'''File for writing buisness logic for grid '''
import traceback
from commons.utils.http_error import HttpError, BadRequest, PymodmValidationError
from grids.validators.grid_validator import GridValidator
from grids.models.grid import Grid

class GridHandler(object):
    '''Grid handler class for handling grid requests'''
    

    def __init__(self):
        '''initializing requierd object'''
        self.validator = GridValidator()
        self.manager = Grid.objects
    
    def store_grid(self, data):
        '''Method to add a grid
        
        Args:
            data: Dict

        Return:
            Tuple (boolean, dict)
        
        Raise:
            PymodmValidationError or BadRequest
        '''
        try:
            nodes = data.get('nodes')
            if len(set(nodes)) != len(nodes):
                return True, 'duplicate node names'
            
            if not self.validator.validate(nodes, data.get('edges')):
                return True, 'All the edges are not connected'
            
            return False, self.manager.add_grid(data, True)
            
        except Exception as e:
            traceback.print_exc()
            if e.__class__.__name__ == 'ValidationError':
                raise PymodmValidationError(e.__str__())
            raise BadRequest(e.__str__())
    
    def get_all_grid(self, offset, size):
        '''Method to get all grids
        
        Args: None
        
        Return:
            Tuple (boolean, list)
        
        Raise:
            HttpError
        '''
        try:
            return self.manager.grid_list(offset=offset, limit=size)
        
        except Exception as e:
            traceback.print_exc()
            raise HttpError(e.__str__())