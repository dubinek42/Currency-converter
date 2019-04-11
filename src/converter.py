import json

rates = {
    "AED": 3.673158,
    "AFN": 77.277458,
    "ALL": 110.95,
    "AMD": 485.716768,
    "ANG": 1.857145,
    "AOA": 318.5175,
    "ARS": 43.09525,
    "AUD": 1.39992,
    "AWG": 1.801247,
    "AZN": 1.7025,
    "BAM": 1.73465,
    "BBD": 2,
    "BDT": 84.348,
    "BGN": 1.738579,
    "BHD": 0.377045,
    "BIF": 1835,
    "BMD": 1,
    "BND": 1.350706,
    "BOB": 6.910207,
    "BRL": 3.828177,
    "BSD": 1,
    "BTC": 0.000189540014,
    "BTN": 69.239464,
    "BTS": 14.1024977679,
    "BWP": 10.571002,
    "BYN": 2.121255,
    "BZD": 2.015827,
    "CAD": 1.333212,
    "CDF": 1636,
    "CHF": 1.002404,
    "CLF": 0.024214,
    "CLP": 662.65,
    "CNH": 6.72171,
    "CNY": 6.716384,
    "COP": 3095.97,
    "CRC": 605.652635,
    "CUC": 1,
    "CUP": 25.75,
    "CVE": 98.2485,
    "CZK": 22.749594,
    "DASH": 0.0075921827,
    "DJF": 178.05,
    "DKK": 6.635316,
    "DOGE": 332.522052632,
    "DOP": 50.615,
    "DZD": 119.35,
    "EAC": 2867.98535556,
    "EGP": 17.348,
    "EMC": 1.2125648612,
    "ERN": 14.997114,
    "ETB": 28.85,
    "ETH": 0.0055415478,
    "EUR": 0.88883,
    "FCT": 0.1116568895,
    "FJD": 2.126404,
    "FKP": 0.763962,
    "FTC": 22.4451027826,
    "GBP": 0.763962,
    "GEL": 2.69,
    "GGP": 0.763962,
    "GHS": 5.235,
    "GIP": 0.763962,
    "GMD": 49.505,
    "GNF": 9225,
    "GTQ": 7.650278,
    "GYD": 209.28461,
    "HKD": 7.83635,
    "HNL": 24.520074,
    "HRK": 6.6002,
    "HTG": 84.641165,
    "HUF": 285.919241,
    "IDR": 14149.975751,
    "ILS": 3.578593,
    "IMP": 0.763962,
    "INR": 69.142197,
    "IQD": 1190,
    "IRR": 42105,
    "ISK": 119.666722,
    "JEP": 0.763962,
    "JMD": 129.28,
    "JOD": 0.709004,
    "JPY": 110.938,
    "KES": 101,
    "KGS": 68.708337,
    "KHR": 4022,
    "KMF": 437.296327,
    "KPW": 900,
    "KRW": 1139.006667,
    "KWD": 0.3042,
    "KYD": 0.833459,
    "KZT": 378.8938,
    "LAK": 8600,
    "LBP": 1507,
    "LD": 260.65,
    "LKR": 174.733735,
    "LRD": 164.000238,
    "LSL": 14.1,
    "LTC": 0.0113365832,
    "LYD": 1.385,
    "MAD": 9.63385,
    "MDL": 17.513226,
    "MGA": 3600,
    "MKD": 54.695,
    "MMK": 1506.240989,
    "MNT": 2512.298805,
    "MOP": 8.07298,
    "MRO": 357,
    "MRU": 36.55,
    "MUR": 34.944512,
    "MVR": 15.450044,
    "MWK": 728.073636,
    "MXN": 18.843818,
    "MYR": 4.1114,
    "MZN": 64.575148,
    "NAD": 14.11,
    "NGN": 360,
    "NIO": 33.02,
    "NMC": 1.0028973491,
    "NOK": 8.515803,
    "NPR": 110.785702,
    "NVC": 0.3852517642,
    "NXT": 26.8466813031,
    "NZD": 1.482886,
    "OMR": 0.385003,
    "PAB": 1,
    "PEN": 3.296772,
    "PGK": 3.382,
    "PHP": 51.8725,
    "PKR": 141.55,
    "PLN": 3.804716,
    "PPC": 1.6623186283,
    "PYG": 6186.225628,
    "QAR": 3.640517,
    "RON": 4.2303,
    "RSD": 104.89,
    "RUB": 64.445,
    "RWF": 901.5,
    "SAR": 3.750663,
    "SBD": 8.174298,
    "SCR": 13.675075,
    "SDG": 47.55,
    "SEK": 9.280691,
    "SGD": 1.35307,
    "SHP": 0.763962,
    "SLL": 8390,
    "SOS": 581,
    "SRD": 7.458,
    "SSP": 130.2634,
    "STD": 21050.59961,
    "STN": 21.825,
    "STR": 7.8941095377,
    "SVC": 8.751385,
    "SYP": 515.016571,
    "SZL": 14.11,
    "THB": 31.77,
    "TJS": 9.434984,
    "TMT": 3.499986,
    "TND": 3.01589,
    "TOP": 2.267408,
    "TRY": 5.695414,
    "TTD": 6.76875,
    "TWD": 30.846317,
    "TZS": 2315.3,
    "UAH": 26.82,
    "UGX": 3758.198709,
    "USD": 1,
    "UYU": 33.969037,
    "UZS": 8450,
    "VEF": 248487.642241,
    "VEF_BLKMKT": 4009.47,
    "VEF_DICOM": 3310.75,
    "VEF_DIPRO": 10,
    "VES": 3303.496849,
    "VND": 23249.900917,
    "VTC": 1.7497929284,
    "VUV": 111.237156,
    "WST": 2.606925,
    "XAF": 583.034552,
    "XAG": 0.06561476,
    "XAU": 0.00076523,
    "XCD": 2.70255,
    "XDR": 0.717524,
    "XMR": 0.0140885606,
    "XOF": 583.034552,
    "XPD": 0.00071814,
    "XPF": 106.065686,
    "XPM": 3.159486081,
    "XPT": 0.0011099,
    "XRP": 2.7996812026,
    "YER": 250.300682,
    "ZAR": 13.92549,
    "ZMW": 12.069,
    "ZWL": 322.355011
}


class Converter:
    def __init__(self, amount, input_currency, output_currency):
        with open('symbols.json', 'r') as symbols_file:
            data = symbols_file.read()
        self.symbols = json.loads(data)
        self.amount = amount
        self.input_currency = self.__symbol_translate(input_currency)
        self.output_currency = self.__symbol_translate(output_currency)
        self.rates = rates

    @staticmethod
    def __is_number(s):
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

    def __calculate(self, amount, input_currency, output_currency):
        if input_currency == "USD":
            return float(self.rates[output_currency]) * float(amount)
        else:
            return float(amount) / float(self.rates[input_currency]) * float(self.rates[output_currency])

    def check_parameters(self):
        if not self.__is_number(self.amount):
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
                output[currency] = self.__calculate(self.amount, self.input_currency, currency)
        else:
            output[self.output_currency] = self.__calculate(self.amount, self.input_currency, self.output_currency)
        result["output"] = output
        return result
