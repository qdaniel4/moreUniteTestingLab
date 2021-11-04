import unittest
from unittest import TestCase
from unittest.mock import patch
import bitcoin

class TestBitCoin(TestCase):
    @patch ('bitcoin.get_bitcoin_exchange')
    def test_convert_btc_to_dollars(self, mock_response):

        # mock response from the API
        mock_response.return_value = {'bpi': {'EUR': {'code': 'EUR',
                 'description': 'Euro',
                 'rate': '52,867.9138',
                 'rate_float': 52867.9138,
                 'symbol': '&euro;'},
         'GBP': {'code': 'GBP',
                 'description': 'British Pound Sterling',
                 'rate': '45,239.3193',
                 'rate_float': 45239.3193,
                 'symbol': '&pound;'},
         'USD': {'code': 'USD',
                 'description': 'United States Dollar',
                 'rate': '61,037.5450',
                 'rate_float': 61037.545,   # Expect the code to find and use this number 
                 'symbol': '&#36;'}},
        'chartName': 'Bitcoin',
        'disclaimer': 'This data was produced from the CoinDesk Bitcoin Price Index '
                    '(USD). Non-USD currency data converted using hourly conversion '
                    'rate from openexchangerates.org',
        'time': {'updated': 'Nov 4, 2021 16:32:00 UTC',
                'updatedISO': '2021-11-04T16:32:00+00:00',
                'updateduk': 'Nov 4, 2021 at 16:32 GMT'}}
        

        # Test converting 100 bitcoin to USD
        expected_dollars = 6103754.5  # 100 times the US rate float value
        actual_dollars  = bitcoin.perform_conversion(100)
        self.assertAlmostEqual(expected_dollars, actual_dollars) #couldn't get the test to work with assertEqual--assertAlmostEqual works fine

if __name__ == '__main__':
    unittest.main()