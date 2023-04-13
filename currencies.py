class Currencies:
    """Hold currency codes and handles validity checks"""

    def __init__(self) -> None:
        """initiate"""
        self.codes = {}

    def check_valid(self, currency):
        """check if code is in codes list"""
        return currency in self.codes
    
    def check_if_num(self, amount):
        """check if amount is a number bigger than 0"""
        try:
            amount_int = int(amount)
        except:
            return False
        return isinstance(amount_int, int) and amount_int >=0
    
    def make_currency_code_list(self, codes):
        """make codes list"""
        self.codes = codes
