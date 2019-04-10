from src.converter import Converter
from connexion import problem


def convert(amount, input_currency, output_currency = ""):
    converter = Converter(amount, input_currency, output_currency)
    if converter.check_parameters():
        return converter.convert()
    else:
        return problem(400, "Bad Request", "Wrong parameters", "about:blank")

