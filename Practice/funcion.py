# Example 1
def add_numbers(x, y, z):
    a = x + y
    b = x + z
    c = y + z
    print(a, b, c)


add_numbers(1, 2, 3)

# Example 2
# Define function with parameters


def product_info(product_name, price):
    print("productname: " + product_name)
    print("Price " + str(price))


# Call function with parameters assigned as above
product_info("White T-shirt", 15)
# Call function with keyword arguments
product_info(product_name="jeans", price=45)

# Example 3
