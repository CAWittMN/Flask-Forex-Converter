class Currencies:
    """handle validity checks"""


    def check_valid(self, currency, codes):
        """check if code is in codes list"""
        try:
            upper_currency = str.upper(currency)
        except:
            return False
        return upper_currency in codes
    
    def check_if_num(self, amount):
        """check if amount is a number bigger than 0"""
        try:
            amount_int = float(amount)
        except:
            return False
        return isinstance(amount_int, float) and amount_int >=0
