#!/usr/bin/env python3

import json
from src.converter import Converter


def convert(amount, input_currency, output_currency):
    converter = Converter(amount, input_currency, output_currency)
    if converter.check_parameters():
        print(json.dumps(converter.convert(), indent=4))
    else:
        print("Wrong parameters. Run with --help for help.")
    

if __name__ == "__main__":
    convert("5.0", "CZK", "USD")
