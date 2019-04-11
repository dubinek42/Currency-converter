import json, time, requests


class Converter:
    def __init__(self, amount, input_currency, output_currency):
        with open('symbols.json', 'r') as symbols_file:
            data = symbols_file.read()
        self.symbols = json.loads(data)
        self.amount = amount
        self.input_currency = self.__symbol_translate(input_currency)
        self.output_currency = self.__symbol_translate(output_currency)
        self.rates = self.__load_rates()

    @staticmethod
    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def __symbol_translate(self, s):
        if s is not None and s != "":
            s = s.upper()
        if s in self.symbols.keys():
            return self.symbols.get(s)
        return s

    def calculate(self, amount, input_currency, output_currency):
        if input_currency == "USD":
            return float(self.rates[output_currency]) * float(amount)
        else:
            return float(amount) / float(self.rates[input_currency]) * float(self.rates[output_currency])

    @staticmethod
    def __load_rates():
        try:
            with open('rates.json', 'r') as rates_file:
                data = rates_file.read()
            rates = json.loads(data)
            time_difference = int(time.time()) - int(rates["timestamp"])
            if time_difference >= 3600:
                raise ValueError()
            return rates["rates"]
        except (ValueError, FileNotFoundError):
            url = "https://openexchangerates.org/api/latest.json?app_id=6bf71ef4de864ee987d2d57d5c78315d&show_alternative=true"
            response = requests.get(url)
            data = response.json()
            with open('rates.json', 'w') as out_file:
                json.dump(data, out_file)
            return data["rates"]

    def check_parameters(self):
        if not self.is_number(self.amount):
            return False
        if self.input_currency not in self.rates.keys():
            return False
        if self.output_currency != "" and self.output_currency is not None:
            if self.output_currency not in self.rates.keys():
                return False
        return True

    def convert(self):
        result = {
            "input": {
                "amount": self.amount,
                "currency": self.input_currency
            }
        }
        output = {}
        if self.output_currency == "" or self.output_currency is None:
            for currency in self.rates.keys():
                output[currency] = round(self.calculate(self.amount, self.input_currency, currency), 6)
        else:
            output[self.output_currency] = round(self.calculate(self.amount, self.input_currency, self.output_currency), 6)
        result["output"] = output
        return result
