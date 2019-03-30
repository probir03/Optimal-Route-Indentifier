'''File for writing buisness logic for grid '''
import traceback
from commons.utils.http_error import HttpError, BadRequest, PymodmValidationError
from grids.validators.grid_validator import GridValidator
from grids.models.grid import Grid
from grids.helpers.helpers import find_optimal_route

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
    
    def get_grid(self, grid_id):
        '''Method to get grid by id

        Args:
            grid_id: str (UUID)
        
        Return:
            tuple (boolean, dict)
        
        Rsise:
            HttpError
        '''
        try:
            grid = self.manager.grid_by_id(grid_id, transform=True)
            if grid:
                return False, grid
            return True, 'Invalid id'
        except Exception as e:
            traceback.print_exc()
            raise HttpError(e.__str__())

    def update_grid(self, grid_id, data):
        '''Method to update grid based on id

        Args:
            grid_id: string(uuid)
            data: dictionary
        
        Return:
            tuple (boolean, dictionary)
        
        Raise:
            HttpError
        '''
        try:
            nodes = data.get('nodes')
            edges = data.get('edges')

            if not self.validator.validate(nodes, edges):
                    return True, 'All the edges are not connected, Failed to update'
                
            err, grid = self.manager.update_grid_by_id(grid_id, data, True)
            if not err:
                return False, grid
            return True, grid if grid else 'Invalid Id'

        except Exception as e:
            traceback.print_exc()
            if e.__class__.__name__ == 'ValidationError':
                raise PymodmValidationError(e.__str__())
            raise BadRequest(e.__str__())
        
    def delete_grid(self, grid_id):
        '''Method to delete a grid by id

        Args:
            grid_id: string(uuid)
        
        Return:
            string
        '''
        try:
            err, res = self.manager.delete_grid_by_id(grid_id)
            if err:
                return err, res
            return err, 'Successfully delete'
        
        except Exception as e:
            traceback.print_exc()
            if e.__class__.__name__ == 'ValidationError':
                raise PymodmValidationError(e.__str__())
            raise BadRequest(e.__str__())
        
    def find_optimal_route(self, grid_id, start, end):
        '''Method to find optimal route between two given nodes

        Args:
            grid_id: string(uuid)
        
        Return:
            tuple (boolean, dict)
        
        Raise:
            HttpError
        '''
        try:
            grid = self.manager.grid_by_id(grid_id, transform=True)
            if grid:
                optimal_route = find_optimal_route(grid.get('edges'), start, end)
                if optimal_route:
                    return False, {"optimalRoute": optimal_route}
                return True, 'There is no route between given point !'
            return True, 'Invalid id'
        except Exception as e:
            traceback.print_exc()
            if e.__class__.__name__ == 'ValidationError':
                raise PymodmValidationError(e.__str__())
            raise BadRequest(e.__str__())
        