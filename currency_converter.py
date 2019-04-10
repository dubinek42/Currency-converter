#!/usr/bin/env python3

import json
from src.converter import Converter


def convert(amount, input_currency, output_currency = ""):
    try:
        converter = Converter(amount, input_currency, output_currency)
        if converter.check_parameters():
            print(json.dumps(converter.convert(), sort_keys=True, indent=4))
        else:
            print("Wrong parameters.")
    except FileNotFoundError:
        print("Cannot find file with currency symbols.")
        exit(-1)
    

if __name__ == "__main__":
    convert("1.0", "CZK")
