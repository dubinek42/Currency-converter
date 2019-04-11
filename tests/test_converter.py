import pytest


@pytest.mark.parametrize("s, expected", [
    ("42", True),
    ("5.012", True),
    ("hello", False),
    ("12g8", False)
])
def test_is_number(s, expected):
    from src.converter import Converter
    
    assert Converter.is_number(s) == expected


@pytest.mark.parametrize("input_currency, output_currency, expected", [
    ("kc", "kČ", ("CZK", "CZK")),
    ("euR", "$", ("EUR", "USD")),
    ("£", "", ("GBP", "")),
    ("kn", "USD", ("HRK", "USD"))
])
def test_currency_symbols(input_currency, output_currency, expected):
    from src.converter import Converter
    converter = Converter(0, input_currency, output_currency)

    assert (converter.input_currency, converter.output_currency) == expected


@pytest.mark.parametrize("input_currency, output_currency, expected", [
    ("kc", "kČ", True),
    ("bla", "bli", False),
    ("czk", "czx", False),
    ("EUR", "USD", True)
])
def test_check_parameters(input_currency, output_currency, expected):
    from src.converter import Converter
    converter = Converter(0, input_currency, output_currency)

    assert converter.check_parameters() == expected


@pytest.mark.parametrize("amount, input_currency, output_currency, expected", [
    (1, "USD", "USD", 1),
    (1, "USD", "ABC", 42),
    (1, "ABC", "ABC", 1),
    (42, "ABC", "USD", 1)
])
def test_calculate(amount, input_currency, output_currency, expected):
    from src.converter import Converter
    converter = Converter(amount, input_currency, output_currency)
    converter.rates = {
        "USD": 1,
        "ABC": 42
    }

    assert converter.calculate(converter.amount, converter.input_currency, converter.output_currency) == expected
