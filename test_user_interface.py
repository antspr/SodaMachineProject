import unittest
from user_interface import try_parse_int, validate_main_menu, get_unique_can_names, display_payment_value, validate_coin_selection
from cans import Cola, OrangeSoda, RootBeer
from coins import Quarter, Dime, Nickel, Penny
class TestValidateMainMenu(unittest.TestCase):
    """Test to see if proper inputs return true"""

    def test_ensure_tuple_one(self):
        """Test to see if one returns tuple one"""
        check = validate_main_menu(1)
        self.assertEqual((True, 1), check)

    def test_ensure_tuple_two(self):
        """Test to see if two returns tuple two"""
        check = validate_main_menu(2)
        self.assertEqual((True, 2), check)

    def test_ensure_tuple_three(self):
        """Test to see if three returns tuple three"""
        check = validate_main_menu(3)
        self.assertEqual((True, 3), check)

    def test_ensure_tuple_four(self):
        """Test to see if four returns tuple four"""
        check = validate_main_menu(4)
        self.assertEqual((True, 4), check)

    def test_ensure_invalid_false(self):
        """Test to see if invalid input returns false"""
        check = validate_main_menu(5)
        self.assertEqual((False, None), check)

class TestTryParseInt(unittest.TestCase):
    """Test to see if values are properly parsed"""

    def test_valid_return(self):
        """Test to see if string is parsed int"""
        check = try_parse_int('10')
        self.assertEqual(10, check)

    def test_invalid_return(self):
        """test to see if invalid input is rejected"""
        check = try_parse_int('none')
        self.assertEqual(0, check)

class TestGetUniqueCanNames(unittest.TestCase):
    """ Test ability to receive unique can names"""
    def test_remove_duplicate_name(self):
        soda_1 = Cola()
        soda_2 = Cola()
        soda_3 = OrangeSoda()
        soda_4 = OrangeSoda()
        soda_5 = RootBeer()
        soda_6 = RootBeer()
        cans = [soda_1, soda_2, soda_3, soda_4, soda_5, soda_6]
        check = get_unique_can_names(cans)
        self.assertEqual(3, len(check))

    def test_append_none_if_empty(self):
        """Test ability to handle invalid inputs"""
        cans = []
        check = get_unique_can_names(cans)
        self.assertEqual(0,len(check))
        

class TestDisplayPaymentValue(unittest.TestCase):
    """Test to display correct total value"""

    def test_proper_value_returned(self):
        """test to ensure payment values equals .41"""
        coins_equals =[Quarter(), Dime(), Nickel(), Penny()]
        check = display_payment_value(coins_equals)
        self.assertEqual(.41, check)

    def test_invalid_value_handled(self):
        """test to ensure no value equals 0 """
        coins_equals = []
        check = display_payment_value(coins_equals)
        self.assertEqual(0, check)
        

class TestValidateCoinSelection(unittest.TestCase):
    """Test to validate coin selection"""
    def test_ensure_tuple_one(self):
        """Test to see if one returns tuple one"""
        check = validate_coin_selection(1)
        self.assertEqual((True, 'Quarter'), check)

    def test_ensure_tuple_two(self):
        """Test to see if two returns tuple two"""
        check = validate_coin_selection(2)
        self.assertEqual((True, 'Dime'), check)

    def test_ensure_tuple_three(self):
        """Test to see if three returns tuple three"""
        check = validate_coin_selection(3)
        self.assertEqual((True, 'Nickel'), check)
    def test_ensure_tuple_four(self):
        """Test to see if four returns tuple four"""
        check = validate_coin_selection(4)
        self.assertEqual((True, 'Penny'), check)
    
    
    def test_ensure_tuple_five(self):
        """Test to see if five returns tuple five"""
        check = validate_coin_selection(5)
        self.assertEqual((True, 'Done'), check)

    
    def test_ensure_invalid_false(self):
        """Test to see if invalid input returns false"""
        check = validate_coin_selection(6)
        self.assertEqual((False, None), check)

if __name__ == '__main__':
    unittest.main()