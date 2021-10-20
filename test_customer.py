import unittest
from customer import Customer
from coins import Dime
from cans import Cola

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

class TestAddCoinsToWallet(unittest.TestCase):
    """ Test that coins can be added to wallet"""
    def setUp(self):
        self.customer = Customer()
    
    def test_add_coins_to_wallet_adds_coins_to_list(self):
        "Adds coins to list"
        wallet_length_check = len(self.customer.wallet.money)
        coins_list = [Dime(), Dime(), Dime()]
        self.customer.add_coins_to_wallet(coins_list)
        self.assertEqual (91, wallet_length_check + 3)

    def test_add_no_coins_to_wallet_adds_no_coins_to_list(self):
        "Adds no coins to wallet"
        wallet_length_check = len(self.customer.wallet.money)
        coins_list = []
        self.customer.add_coins_to_wallet(coins_list)
        self.assertEqual (88, wallet_length_check)

class TestAddCanToBackpack(unittest.TestCase):
    """Test that can can be added to backpack"""
    def setUp(self):
        self.customer = Customer()

    def test_can_add_cola_to_backpack(self):
        """Adds can to backpack"""
        backpack_length_check = len(self.customer.backpack.purchased_cans)
        self.customer.add_can_to_backpack(Cola())
        self.assertEqual(1, backpack_length_check + 1)

    def test_check_if_cola_name(self):
        """Check if what was added is Cola""" 
        self.customer.add_can_to_backpack(Cola())
        can_name_check = self.customer.backpack.purchased_cans[0].name
        self.assertEqual('Cola', can_name_check)
    
    def test_check_if_cola_price(self):
        """Check if what was added is Cola's price""" 
        self.customer.add_can_to_backpack(Cola())
        can_price_check = self.customer.backpack.purchased_cans[0].price
        self.assertEqual(.60, can_price_check)


if __name__ == '__main__':
    unittest.main()