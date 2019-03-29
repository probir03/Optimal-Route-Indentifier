'''test file for grid view'''
# coding: utf-8
from __future__ import unicode_literals

import json
from rest_framework.test import APIRequestFactory

from commons.utils.http_error import HttpError, BadRequest, PymodmValidationError
from grids.views.grid_views import GridViewSet

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
        '''Tets get method of grif biew set'''
        factory = APIRequestFactory()
        view = GridViewSet.as_view()
        request = factory.get('/grids')
        response = view(request)
        self.assertEqual(response.status_code, 200)