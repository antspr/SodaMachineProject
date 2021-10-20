import unittest
from wallet import Wallet

class TestWallet(unittest.TestCase):
    """ Test to that wallet has all 88 coins"""
    def setUp(self):
        self.wallet = Wallet()
    
    def test_wallet_has_money(self):
        """Test Wallet class is instantiated with all coins"""
        wallet_count = len(self.wallet.money)
        self.assertEqual(88, wallet_count)

if __name__ == "__main__":
    unittest.main()
