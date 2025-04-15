import unittest
from discount_price_calculator import DiscountPriceCalculator

class TestCaculator(unittest.TestCase):
    
    def test_calculate_discount(self):
        discount = DiscountPriceCalculator(30.00, 50).calculate_discount()
        self.assertEqual(discount, 15)
        
    
    def test_calculate_discounted_price(self):
        discounted_price = DiscountPriceCalculator(30.00, 15).calculate_discounted_price()
        self.assertEqual(discounted_price, 25.5)
        

        
