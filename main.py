
from discount_price_calculator import DiscountPriceCalculator

price = input("Enter the price: ")
discount_per = input("Enter the discount percentage: ")

discount_price_calculate = DiscountPriceCalculator(price, discount_per)

discount = discount_price_calculate.calculate_discount()

discounted_price = discount_price_calculate.calculate_discounted_price()

print(f"The price after {discount} Euros discount is: {discounted_price} Euros")