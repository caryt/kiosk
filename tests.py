"""Unit Tests for the Kiosk Application.
"""
import kiosk
import unittest
from flask import request
from datetime import date
from utils import years_between

class KioskTestCase(unittest.TestCase):
    """Test the Web Site.
    """

    def setUp(self):
        kiosk.app.config['TESTING'] = True
        self.app = kiosk.app.test_client()

    def tearDown(self):
        pass

    def login(self, username, password):
        return self.app.post('/', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_login_page(self):
        rv = self.app.get('/')
        assert 'Username' in rv.data
        assert 'Password' in rv.data

    def test_not_logged_in(self):
        rv = self.app.get('/department')
        assert 'You are not logged in' in rv.data

    def test_login_Georgi(self):
        rv = self.login('Georgi.Facello', '10001')
        assert 'You were logged in' in rv.data
        assert 'Georgi Facello' in rv.data

    def test_login_invalid(self):
        rv = self.login('Georgi.Facello', '10002')
        assert 'Invalid username / password' in rv.data
        rv = self.login('Georgi.FacellX', '10001')
        assert 'Invalid username / password' in rv.data

class UtilsTestCase(unittest.TestCase):
    """Tests for the Utility Functions.
    """

    def test_years_between(self):
        assert years_between(date(1963, 12, 7), date(2014, 12, 6)) == 50
        assert years_between(date(1963, 12, 7), date(2014, 12, 7)) == 51
        assert years_between(date(1963, 12, 7), date(2014, 12, 8)) == 51

if __name__ == '__main__':
    unittest.main()