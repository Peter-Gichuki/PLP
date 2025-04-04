#a python script to calculate the discounted price of an item based on a given discount percentage.
price = int(input("Enter the original price: "))
discount_percent = int(input("Enter the discount percentage: "))

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        price =price -(price *discount_percent/100)
        return price
    else:
        return price
    
discounted_price = calculate_discount(price, discount_percent)
print(f"The discounted price is: {discounted_price}")


