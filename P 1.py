class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product ID: {self.product_id}, Name: {self.name}, Price: ${self.price:.2f}"


class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, product, quantity=1):
        for item in self.cart:
            if item['product'] == product:
                item['quantity'] += quantity
                print(f"Added {quantity} {product.name}(s) to the cart.")
                return

        self.cart.append({'product': product, 'quantity': quantity})
        print(f"Added {quantity} {product.name}(s) to the cart.")

    def display_cart(self):
        if not self.cart:
            print("The cart is empty.")
        else:
            print("Shopping Cart:")
            for item in self.cart:
                product = item['product']
                quantity = item['quantity']
                print(f"{product.name} x {quantity} - ${product.price * quantity:.2f}")

    def calculate_total(self):
        total_cost = sum(item['product'].price * item['quantity'] for item in self.cart)
        return total_cost


class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.shopping_cart = ShoppingCart()

    def __str__(self):
        return f"Customer ID: {self.customer_id}, Name: {self.name}"
    
product1 = Product(1, "Laptop", 1200.00)
product2 = Product(2, "Headphones", 50.00)
product3 = Product(3, "Mouse", 20.00)

customer1 = Customer(101, "John Doe")

customer1.shopping_cart.add_to_cart(product1, 2)
customer1.shopping_cart.add_to_cart(product2, 1)
customer1.shopping_cart.add_to_cart(product3, 3)

customer1.shopping_cart.display_cart()

total_cost = customer1.shopping_cart.calculate_total()
print(f"Total cost: ${total_cost:.2f}")
