class Currencies:
    def __init__(self) -> None:
        self.codes = {}

    def check_valid(self, to, from_curr):
        return to and from_curr in self.codes
    
    def check_if_num(self, amount):
        return isinstance(amount, int)
    
    def make_currency_code_list(self, codes):
        self.codes = codes
