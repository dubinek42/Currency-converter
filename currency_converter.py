#!/usr/bin/env python3

import json
import argparse
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
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--amount", type=float, required=True)
    parser.add_argument("-i", "--input_currency", type=str, required=True)
    parser.add_argument("-o", "--output_currency", type=str, required=False)
    args = parser.parse_args()
    convert(args.amount, args.input_currency, args.output_currency)
