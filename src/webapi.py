import converter

TESTOBJECT = {
    "input": {
        "amount": 0.9,
        "currency": "CNY"
    },
    "output": {
        "AUD": 0.20,
        "CZK": "moc",
    }
}

def convert(amount, input_currency, output_currency = ""):
    if converter.check_parameters(amount, input_currency, output_currency):
        return TESTOBJECT
    else:
        return False
