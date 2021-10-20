import unittest
from customer import Customer

class TestGetWalletCoin(unittest.TestCase):
    """Test that each type of coin can be returned from Wallet"""

    def setUp(self):
        self.customer = Customer()

    def test_quarter_string_returns_quater_instance(self):
        """Test that quarter is returned from wallet"""
        returned_coin = self.customer.get_wallet_coin('Quarter')  
        self.assertEqual('Quarter', returned_coin.name)

    def test_dime_string_returns_dime_instance(self):
        """Test that dime is returned from wallet"""
        returned_coin = self.customer.get_wallet_coin('Dime')  
        self.assertEqual('Dime', returned_coin.name)  

    def test_nickel_string_returns_nickel_instance(self):
        """Test that nickel is returned from wallet"""
        returned_coin = self.customer.get_wallet_coin('Nickel')  
        self.assertEqual('Nickel', returned_coin.name)  

    def test_penny_string_returns_penny_instance(self):
        """Test that penny is returned from wallet"""
        returned_coin = self.customer.get_wallet_coin('Penny')  
        self.assertEqual('Penny', returned_coin.name)    

    def test_invalid_string_returns_none(self):
        """Test that penny is returned from wallet"""
        returned_coin = self.customer.get_wallet_coin('Rubie')  
        self.assertEqual(None, returned_coin)    

if __name__ == '__main__':
    unittest.main()