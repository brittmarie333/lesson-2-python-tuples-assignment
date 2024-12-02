#You are given a list of tuples, each representing a customer's order. 
#Each tuple contains the customer's name, the product ordered, and the quantity. 
#Your task is to unpack each tuple and print the order details in a user-friendly format.
#Sample Order Data:
#orders = [
 #   ("Alice", "Laptop", 1),
 #   ("Bob", "Camera", 2),
    # More orders...]

#Write a function to iterate over the list of orders. 
# - Unpack each tuple in the list and format the details for display.

def print_order_details(orders):
    for order in orders:
        customer_name, product_name, quantity = order
        print(f"Customer: {customer_name}\nProduct: {product_name}\nQuantity: {quantity}\n{'-'*30}")

orders = [
    ("Britt", "XBox S", 1),
    ("Ron", "", 2),
    ("Charlie", "Phone", 3)
]

# Call the function to print the order details
print_order_details(orders)
