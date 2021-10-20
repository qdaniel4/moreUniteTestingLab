import requests
from pprint import pprint
def main():
    bitcoin_amount = get_input()
    exchange_rate = get_bitcoin_exchange()
    dollars = get_dollar_amount(bitcoin_amount, exchange_rate)
    outputs(bitcoin_amount, dollars)

def get_input():
    bitcoin_amount = input('Enter bitcoin amount: ')
    while bitcoin_amount.isnumeric() is False or int(bitcoin_amount) <= 0:
        print('Error: bitcoin amount must be a number greater than 0\n')
        bitcoin_amount = input('Enter bitcoin amount: ')
    bitcoin_amount = float(bitcoin_amount)
    return bitcoin_amount

#going to mock this function
def get_bitcoin_exchange():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    data = requests.get(url).json()
    pprint(data)
    exchange_rate = data.get('bpi').get('USD').get('rate_float')
    exchange_rate = float(exchange_rate)
    return exchange_rate

def get_dollar_amount(bitcoin_amount, exchange_rate):
    dollars = bitcoin_amount * exchange_rate
    return dollars

def outputs(bitcoin_amount, dollars):
    print(f'{bitcoin_amount:.2f} BTC = ${dollars:.2f} USD')


if __name__ == '__main__':
    main()