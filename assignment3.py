# Function definition
def calculate_discount(price, discount_percent):
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        # Calculate the final price after applying the discount
        return price - (price * discount_percent / 100)
    else:
        # Return the original price if the discount is less than 20%
        return price

# Prompt the user for the original price and discount percentage
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Call the function and calculate the final price
    final_price = calculate_discount(price, discount_percent)

    # Print the result
    if discount_percent >= 20:
        print(f"The final price after applying the discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The original price is: {final_price:.2f}")
except ValueError:
    print("Please enter valid numbers for price and discount percentage.")
