class DiscountPriceCalculator:
    
    def __init__(self, price: float, discount_per: int)->float:
        self.price = price
        self.discount_per = discount_per
    
        
    def calculate_discount(self)->float:
        discount = self.price*self.discount_per/100
        return discount
        
        
    def calculate_discounted_price(self)->float:
        discounted_price = self.price - self.calculate_discount()
        return discounted_price
        