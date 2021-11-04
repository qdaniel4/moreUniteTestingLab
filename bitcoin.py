import requests
from pprint import pprint
def main():
    bitcoin_amount = get_input()
    dollars = perform_conversion(bitcoin_amount)
    outputs(bitcoin_amount, dollars)

def get_input():
    bitcoin_amount = input('Enter bitcoin amount: ')
    while bitcoin_amount.isnumeric() is False or int(bitcoin_amount) <= 0:
        print('Error: bitcoin amount must be a number greater than 0\n')
        bitcoin_amount = input('Enter bitcoin amount: ')
    bitcoin_amount = float(bitcoin_amount)
    return bitcoin_amount


def perform_conversion(bitcoin_amount):
    api_data = get_bitcoin_exchange()
    usd_rate = get_usd_rate(api_data)
    dollars = get_dollar_amount(bitcoin_amount, usd_rate)
    return dollars

# going to mock this function - keep this simpler and smaller. Want to mock as little code as possible
# so the test is checking as much of your code as possible.
def get_bitcoin_exchange():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    data = requests.get(url).json()
    return data 

def get_usd_rate(data):
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