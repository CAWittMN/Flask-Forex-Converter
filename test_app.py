from app import app
from flask import session   
from currencies import Currencies
from unittest import TestCase

app.config['TESTING'] = True

currency_checker = Currencies()

class ForexConverterTests(TestCase):
    
    def test_code_check(self):
        """test if input value is a valid currency code"""

        codes = {'USD': 'Us dolars', 'PLN': 'Polis Zloty'}
        self.assertTrue(currency_checker.check_valid('USD', codes))
        self.assertFalse(currency_checker.check_valid('POO', codes))
        self.assertFalse(currency_checker.check_valid(345, codes))

    def test_amount_check(self):
        """test if number is a float above 0"""

        self.assertTrue(currency_checker.check_if_num(500))
        self.assertFalse(currency_checker.check_if_num(-55))
        self.assertFalse(currency_checker.check_if_num('string'))

    def test_home_page(self):
        """test home page displays"""

        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('CONVERT', html)

    def test_redirect_check(self):

        with app.test_client() as client:
            res = client.post('/check-values')
            self.assertEqual(res.status_code, 302)
            self.assertEqual(res.location, '/')

    def test_session_codes(self):
        """test session codes download and post"""

        with app.test_client() as client:
            res = client.get('/')
            self.assertEqual(res.status_code, 200)
            self.assertNotEqual(session['codes'], {})

    def test_convertion(self):
        """test convertion"""

        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['from'] = 'USD'
                sess['to'] = 'USD'
                sess['amount'] = 100
                sess['success'] = True
            res = client.get('/converted')
            
            self.assertEqual(session.get('result'), '100.00')

    def test_convertion_redirect(self):
        """test accessing convertion too early"""
        
        with app.test_client() as client:
            with client.session_transaction() as sess:
                sess['success'] = False
            res = client.get('/converted')
            self.assertEqual(res.location, '/')


