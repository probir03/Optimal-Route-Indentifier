'''test file for grid view'''
# coding: utf-8
from __future__ import unicode_literals

import json
from rest_framework.test import APIRequestFactory

from commons.utils.http_error import HttpError, BadRequest, PymodmValidationError
from grids.views.grid_views import GridViewSet, EachGridViewSet, OptimalRouteViewSet
from grids.handlers.grid_handler import GridHandler

from ..base_test import BaseTest
from ..dummy_schema import get_dummy_valid_grid
from ..dummy_schema import get_dummy_invalid_grid

class TestGridViews(BaseTest):
    '''Test class for grid view'''

    def test_post_grid_view_set(self):
        '''Tets post method of grif biew set'''
        factory = APIRequestFactory()
        view = GridViewSet.as_view()
        request = factory.post('/grids', json.dumps(get_dummy_valid_grid()),
                               content_type='application/json')
        response = view(request)
        self.assertEqual(response.status_code, 201)
    
    def test_get_grid_view_set(self):
        '''Tets get method of grid view set'''
        factory = APIRequestFactory()
        view = GridViewSet.as_view()
        request = factory.get('/grids')
        response = view(request)
        self.assertEqual(response.status_code, 200)
    
    def test_get_each_grid_view_set(self):
        '''Tets get method of each grid view set'''
        handler_obj = GridHandler()
        err, res = handler_obj.store_grid(get_dummy_valid_grid(name='test_get_each_grid'))
        
        factory = APIRequestFactory()
        view = EachGridViewSet.as_view()
        request = factory.get('/grids/' + res.get('id'))
        response = view(request, res.get('id'))
        self.assertEqual(response.status_code, 200)
    
    def test_update_each_grid_view_set(self):
        '''Tets put method of each grid view set'''
        handler_obj = GridHandler()
        err, res = handler_obj.store_grid(get_dummy_valid_grid(name='test_update_each_grid'))

        factory = APIRequestFactory()
        view = EachGridViewSet.as_view()
        request = factory.put('/grids/' + res.get('id'), json.dumps(get_dummy_valid_grid('test_update_each_grid1')),
                               content_type='application/json')
        response = view(request, res.get('id'))
        self.assertEqual(response.status_code, 200)
    
    def test_delete_each_grid_view_set(self):
        '''Tets delte method of each grid view set'''
        handler_obj = GridHandler()
        err, res = handler_obj.store_grid(get_dummy_valid_grid(name='test_delete_each_grid'))

        factory = APIRequestFactory()
        view = EachGridViewSet.as_view()
        request = factory.delete('/grids' + res.get('id'))
        response = view(request, res.get('id'))
        self.assertEqual(response.status_code, 200)
    
    def test_optimal_route_view_set(self):
        '''Tets delte method of each grid view set'''
        handler_obj = GridHandler()
        err, res = handler_obj.store_grid(get_dummy_valid_grid(name='test_optimal_each_grid'))

        factory = APIRequestFactory()
        view = OptimalRouteViewSet.as_view()
        request = factory.get('/grids' + res.get('id') + '?start=a&end=b')
        response = view(request, res.get('id'))
        self.assertEqual(response.status_code, 200)