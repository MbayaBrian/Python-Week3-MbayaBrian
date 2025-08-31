''' Week 3 Assignment - 
        Conditionals, Functions, and general Control Flow
'''
''' Question 1.
    A function called calculate_discount that calculates final price after applying discount.
    Only applies discount if discount_percent >= 20.
    '''

def calculate_discount(price, discount_percent):

    
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price


# Prompting user for inputs
try:
    price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate final price
    # Invoking the calculate_discount function
    final_price = calculate_discount(price, discount_percent)

    # Output result
    if discount_percent >= 20:
        print(f"Discount applied! Final price: {final_price:.2f}")
    else:
        print(f"No discount applied. Final price: {final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for price and discount.")
