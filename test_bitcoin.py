import unittest
from unittest import TestCase
from unittest.mock import patch
import bitcoin

class TestBitCoin(TestCase):
    @patch ('bitcoin.get_bitcoin_exchange')
    def test_convert_btc_to_dollars(self, mock_response):
        mock_response.return_value = 987789.121654

        expected = mock_response.return_value * 50
        exchange = bitcoin.get_bitcoin_exchange()
        actual = bitcoin.get_dollar_amount(50, exchange)
        self.assertAlmostEqual(expected, actual) #couldn't get the test to work with assertEqual--assertAlmostEqual works fine
if __name__ == '__main__':
    unittest.main()