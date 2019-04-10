class Converter:
    def __init__(self, amount, input_currency, output_currency):
        self.amount = amount
        self.input_currency = input_currency
        self.output_currency = output_currency

    def __is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def check_parameters(self):
        if self.__is_number(self.amount):
            return True
        else:
            return False

    def convert(self):
        test_object = {
            "input": {
                "amount": 0.9,
                "currency": "CNY"
            },
            "output": {
                "AUD": 0.20,
                "CZK": "moc",
            }
        }
        return test_object








def check_parameters(amount, input_currency, output_currency = ""):
    return True
