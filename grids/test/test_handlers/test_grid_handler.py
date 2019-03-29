'''test file for grid handler'''
# coding: utf-8
from __future__ import unicode_literals

from commons.utils.http_error import HttpError, BadRequest, PymodmValidationError
from grids.handlers.grid_handler import GridHandler

from ..base_test import BaseTest
from ..dummy_schema import get_dummy_valid_grid
from ..dummy_schema import get_dummy_invalid_grid


class TestGridHandle(BaseTest):
    '''Test class for Grid Handler'''

    def test_store_grid(self):
        '''Test store_grid success'''
        handler_obj = GridHandler()
        err, res = handler_obj.store_grid(get_dummy_valid_grid())
        self.assertEqual(err, False)

    def test_store_grid_with_duplicate_name(self):
        '''Test for duplicate name'''
        self.assertRaises(PymodmValidationError, GridHandler().store_grid, get_dummy_valid_grid())
    
    def test_store_grid_with_wrong_grid(self):
        '''Tets for a wrong grid'''
        handler_obj = GridHandler()
        err, res = handler_obj.store_grid(get_dummy_invalid_grid())
        self.assertEqual(err, True)

    def test_get_all_grid(self):
        ''' Test get_all_grid method'''
        handler_obj = GridHandler()
        res, count, offset = handler_obj.get_all_grid(0, 10)
        self.assertEqual(count, 0)