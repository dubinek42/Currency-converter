# Currency-converter
Kiwi.com entry task - currency converter CLI and web API application.

[![Build Status](https://travis-ci.com/dubinek42/Currency-converter.svg?token=JHuza4cY5JycVgsEpGRq&branch=master)](https://travis-ci.com/dubinek42/Currency-converter)

## CLI application
### Installation
(Python 3 needed)
```
pip install -r requirements.txt
```
### Usage
```
./currency_converter.py [--help] --amount <amount> --input_currency <currency_symbol> [--output_currency <currency_symbol>]
```

#### Example
```
./currency_converter.py --amount 5.0 --input_currency USD --output_currency Kč
```


## Web API application
### Run server
```
docker-compose build
docker-compose up
```
### Usage
Server listens on port 5000
```
http://localhost:5000/currency_converter?amount=<amount>&input_currency=<symbol>&output_currency=<symbol>
```
#### Example
```
http://localhost:5000/currency_converter?amount=5.0&input_currency=USD&output_currency=CZK
```
### Swagger UI
Try out the API in this intuitive GUI:
```
http://localhost:5000/ui
```

## Tests
```
python -m pytest tests/
```
