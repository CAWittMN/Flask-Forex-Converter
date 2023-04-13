from unittest import TestCase
from app import app
from currencies import Currencies

currencies = Currencies()

class ForexConverterTests(TestCase):
    def setUp(self):
        currencies.make_currency_code_list({'USD': 'Us dolars', 'PLN': 'Polis Zloty'})