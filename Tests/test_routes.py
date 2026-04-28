'''
Tests for Flask routes in app.py.
Tests cover both literacy rate and average education.
'''

import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from app import app
from ProductionCode.command_line import load_data

load_data()


class TestLiteracyGrowthRoute(unittest.TestCase):
    '''Tests for the /literacy-growth/<country> route.'''

    def setUp(self):
        self.client = app.test_client()

    def test_valid_country(self):
        '''A real country should return a 200 status with its name and a percentage.'''
        response = self.client.get('/literacy-growth/France')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'France', response.data)
        self.assertIn(b'%', response.data)

    def test_hyphen_converted_to_space(self):
        '''Hyphens in the URL should be converted to spaces.'''
        response = self.client.get('/literacy-growth/United-States')
        self.assertIn(b'United States', response.data)

    def test_invalid_country(self):
        '''A country not in the dataset should return a no-data message.'''
        response = self.client.get('/literacy-growth/Nonexistentland')
        self.assertIn(b'No literacy data', response.data)


class TestSchoolingRoute(unittest.TestCase):
    '''Tests for the /schooling/<country>/<start_year>/<end_year> route.'''

    def setUp(self):
        self.client = app.test_client()

    def test_valid_country_and_years(self):
        '''Tests a valid country and year range should return data with the country name.'''
        response = self.client.get('/schooling/France/2000/2020')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'France', response.data)
        self.assertIn(b'years', response.data)

    def test_invalid_year_range(self):
        '''Start year greater than end year should return an error message'''
        response = self.client.get('/schooling/France/2020/2000')
        self.assertIn(b'appropriate', response.data)

    def test_invalid_country(self):
        '''Test for a country not in the dataset should return none'''
        response = self.client.get('/schooling/Nonexistentland/2000/2020')
        self.assertIn(b'No data found', response.data)

    def test_no_data_in_year_range(self):
        '''A valid country with no data in the given range should return none'''
        response = self.client.get('/schooling/France/1800/1801')
        self.assertIn(b'No data found', response.data)


if __name__ == '__main__':
    unittest.main()