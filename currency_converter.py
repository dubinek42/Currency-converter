#!/usr/bin/env python3

import json, src.converter
Converter = src.converter

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

def convert(amount, input_currency, output_currency):
    if Converter.check_parameters(amount, input_currency, output_currency):
        print(json.dumps(TESTOBJECT, indent=4))
    else:
        return False
    

if __name__ == "__main__":
    convert(5.0, "CZK", "USD")
