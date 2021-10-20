import unittest
from coins import Quarter, Dime, Nickel, Penny
from soda_machine import SodaMachine
from cans import Cola

class TestFillRegister(unittest.TestCase):
    """Test register has money in it"""

    def setUp(self):
        self.sodamachine = SodaMachine()
    
    def test_fill_register(self):
        """Test to see if register has money in it"""
        self.assertEqual(88, len(self.sodamachine.register))

class TestFillInventory(unittest.TestCase):
    """Test inventory has inventory"""

    def setUp(self):
        self.sodamachine = SodaMachine()

    def test_fill_inventory(self):
        """Test to see if inventory has product in it"""
        self.assertEqual(30, len(self.sodamachine.inventory))            

class TestGetCoinFromRegister(unittest.TestCase):
    """Test each type of coin can be returned from register"""

    def setUp(self):
        self.sodamachine = SodaMachine()

    def test_get_quarter_from_register(self):
        """Test to see if Quarter can be returned from Register"""
        coin_check = self.sodamachine.get_coin_from_register('Quarter')
        self.assertEqual(.25, coin_check.value)

    def test_get_dime_from_register(self):
        """Test to see if Dime can be returned from Register"""
        coin_check = self.sodamachine.get_coin_from_register('Dime')
        self.assertEqual(.10, coin_check.value) 

    def test_get_nickel_from_register(self):
        """Test to see if Nickel can be returned from Register"""
        coin_check = self.sodamachine.get_coin_from_register('Nickel')
        self.assertEqual(.05, coin_check.value) 

    def test_get_penny_from_register(self): 
        """Test to see if Penny can be returned from Register"""
        coin_check = self.sodamachine.get_coin_from_register('Penny')
        self.assertEqual(.01, coin_check.value)   

    def test_invalid_str_from_register(self):
        """Test to see if and empty string will return None from Register"""
        coin_check = self.sodamachine.get_coin_from_register('')
        self.assertEqual(None, coin_check)

class TestRegisterHasCoin(unittest.TestCase):
    """Test that register has each type of coin"""

    def setUp(self):
        self.sodamachine = SodaMachine()

    def test_is_quater_true(self):
        """Test to see if Quarter is True"""
        bool_check = self.sodamachine.register_has_coin('Quarter')
        self.assertEqual(True, bool_check)

    def test_is_dime_true(self):
        """Test to see if Dime is True"""
        bool_check = self.sodamachine.register_has_coin('Dime')
        self.assertEqual(True, bool_check)

    def test_is_nickel_true(self):
        """Test to see if Nickel is True"""
        bool_check = self.sodamachine.register_has_coin('Nickel')
        self.assertEqual(True, bool_check)

    def test_is_penny_true(self):
        """Test to see if Penny is True"""
        bool_check = self.sodamachine.register_has_coin('Penny')
        self.assertEqual(True, bool_check)

    def test_is_invalid_false(self):
        """Test to see if invalid input is False"""
        bool_check = self.sodamachine.register_has_coin('Rubie')
        self.assertEqual(False, bool_check)    

class TestDetermineChangeValue(unittest.TestCase):
    """Test that change value can be determined"""

    def setUp(self):
        self.sodamachine = SodaMachine()

    def test_total_payment_higher(self):
        """Test to see if correct output if total payment is higher than can price"""
        change = self.sodamachine.determine_change_value(.70, self.sodamachine.inventory[0].price)
        self.assertEqual(.10, change)

    def test_select_soda_price_higher(self):
        """Test to see if correct output if can price is higher than total payment"""
        change = self.sodamachine.determine_change_value(.50, self.sodamachine.inventory[0].price)
        self.assertEqual(-0.10, change)

    def test_if_price_payment_are_equal(self):
        """Test to see if correct output if total payment and can price are equal"""
        change = self.sodamachine.determine_change_value(.60, self.sodamachine.inventory[0].price) 
        self.assertEqual(0, change)   

class TestCalculateCoinValue(unittest.TestCase):
    """Test to see if coin value is properly calculated"""

    def setUp(self):
        self.sodamachine = SodaMachine()
        self.coin_list = [Quarter(), Nickel(), Dime(), Penny()]

    def test_proper_value_returned(self):
        """Test to see if properly calculates all coins"""
        value = self.sodamachine.calculate_coin_value(self.coin_list)
        self.assertEqual(.41, value)    

    def test_invalid_value(self):
        """Test to see if handles no coins to calculate properly"""
        value = self.sodamachine.calculate_coin_value([])
        self.assertEqual(0, value)

class TestGetInventorySoda(unittest.TestCase):
    """Test to see if Soda can be found"""

    def setUp(self):
        self.sodamachine = SodaMachine()

    def test_find_cola(self):
        """Test to see if Cola can be found"""
        check_soda = self.sodamachine.get_inventory_soda('Cola')
        self.assertEqual(.60, check_soda.price)

    def test_find_orange_soda(self):
        """Test to see if Orange Soda can be found"""
        check_soda = self.sodamachine.get_inventory_soda('Orange Soda')
        self.assertEqual(.40, check_soda.price)   

    def test_find_root_beer(self):
        """Test to see if Root Beer can be found"""
        check_soda = self.sodamachine.get_inventory_soda('Root Beer')
        self.assertEqual(.50, check_soda.price)    

    def test_find_invalid(self):    
        """Test to see if invalid is handled properly"""
        check_soda = self.sodamachine.get_inventory_soda('Mountain Dew')
        self.assertEqual(None, check_soda)

class TestReturnInventory(unittest.TestCase):
    """Test to see Soda can be added to Inventory"""

    def setUp(self):
        self.sodamachine = SodaMachine()

    def test_can_added_to_inventory(self):
        self.sodamachine.return_inventory(Cola())
        self.assertEqual(31, len(self.sodamachine.inventory))    

class TestDepositCoinsIntoRegister(unittest.TestCase):
    """Test to see if coins can be added to register"""

    def setUp(self):
        self.sodamachine = SodaMachine()
        self.coin_list = [Quarter(), Dime(), Nickel(), Penny()]        

    def test_coins_added_to_register(self):
        self.sodamachine.deposit_coins_into_register(self.coin_list)
        self.assertEqual(92, len(self.sodamachine.register))    

if __name__ ==  '__main__':
    unittest.main()