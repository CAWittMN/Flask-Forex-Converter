class Currencies:
    def __init__(self) -> None:
        self.codes = {}

    def check_valid_currency(self, code):
        return code in self.currencies
    
    def check_if_num(self, amount):
        return isinstance(amount, int)
    
    def make_currency_code_list(self, codes):
        self.codes = codes
