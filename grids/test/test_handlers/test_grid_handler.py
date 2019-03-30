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
    
    def test_get_grid(self):
        ''' Test get_grid method'''
        handler_obj = GridHandler()
        err, res = handler_obj.store_grid(get_dummy_valid_grid('grid by id'))
        err, res = handler_obj.get_grid(res.get('id'))
        self.assertEqual(err, False)
    

    def test_update_grid(self):
        ''' Test update_grid method'''
        handler_obj = GridHandler()
        err, res = handler_obj.store_grid(get_dummy_valid_grid('update grid by id'))
        res['name'] = 'update grid'
        err, res = handler_obj.update_grid(res.pop('id'), res)
        self.assertEqual(err, False)
    
    def test_delete_grid(self):
        ''' Test delete_grid method'''
        handler_obj = GridHandler()
        err, res = handler_obj.store_grid(get_dummy_valid_grid('delete grid by id'))
        err, res = handler_obj.delete_grid(res.get('id'))
        self.assertEqual(err, False)
    
    def test_optimal_route(self):
        ''' Test update_grid method'''
        handler_obj = GridHandler()
        err, res = handler_obj.store_grid(get_dummy_valid_grid('optimal grid by id'))
        err, res = handler_obj.find_optimal_route(res.pop('id'), 'a', 'b')
        self.assertEqual(err, False)
    
    def test_no_optimal_route(self):
        ''' Test update_grid method'''
        handler_obj = GridHandler()
        err, res = handler_obj.store_grid(get_dummy_valid_grid('no optimal grid by id'))
        err, res = handler_obj.find_optimal_route(res.pop('id'), 'a', 'x')
        self.assertEqual(err, True)