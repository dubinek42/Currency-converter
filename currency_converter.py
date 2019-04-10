#!/usr/bin/env python3

import json

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
    print(json.dumps(TESTOBJECT, indent=4))

if __name__ == "__main__":
    convert()
