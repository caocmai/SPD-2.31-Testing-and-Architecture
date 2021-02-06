# Adapted from a Java code in the "Refactoring" book by Martin Fowler.
# Replace temp with query
# Code snippet. Not runnable.
def get_price(quantity, item_price):
    # base_price = quantity * item_price
    discount_factor = 0
    if base_price(quantity, item_price) > 1000: 
        discount_factor = 0.95
    else: 
        discount_factor = 0.98
    return base_price(quantity, item_price) * discount_factor

def base_price(quantity, item_price):
    return quantity * item_price

