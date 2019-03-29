from rest_framework.views import APIView
from commons.utils.response import JSONResponse, Created, OK
from commons.utils.http_error import HttpError, BadRequest, PymodmValidationError
from grids.handlers.grid_handler import GridHandler

class GridViewSet(APIView):
    '''View class for Gride
       will Process GET (get all grid) and POST(add a grid)request for gride
    '''

    def __init__(self):
        '''Initializer method for GridViewSet'''
        self.handler_obj = GridHandler()

    def get(self, request):
        '''get function process GET request
        Args:
            request: Request Object
        
        Return:
            JSONResponse
        '''
        offset = int(request.query_params.get('offset', 0))
        size = int(request.query_params.get('size', 10))
        res, count, offset = self.handler_obj.get_all_grid(offset, size)

        return JSONResponse({'data': res, 'message': 'success', 'statusCode': 200,
                        'count': count, 'offset': offset})

    def post(self, request):
        '''get function process POST request
        Args:
            request: Request Object
        
        Return:
            JSONResponse
        '''
        data = request.data
        err, res = self.handler_obj.store_grid(data)
        if err:
            raise BadRequest(400, res)
        return Created({'data': res, 'message': 'success', 'statusCode': 201})


class EachGridViewSet(APIView):
    '''View class for Gride
       will Process GET, POST, DELETE, UPDATE request for each gride
    '''

    def __init__(self):
        '''Initialize method for EachGridViewSet'''
        self.handler_obj = GridHandler()

    def get(self, request, grid_id):
        '''get function to get each Gride
        
        Args:
            request: Request object
            grid_id: String(UUID)

        Return:
            JSONResponse
        '''
        #get each grid
        pass
    
    def put(self, request, grid_id):
        '''Update method for each Gride
        
        Args:
            request: Request object
            grid_id: String(UUID)

        Return:
            JSONResponse
        '''
        #update each grid
        pass
    
    def delete(self, request, grid_id):
        '''DELETE method for each Gride
        
        Args:
            request: Request object
            grid_id: String(UUID)

        Return:
            JSONResponse
        '''
        #delete each grid
        pass