# Thomas-POS_Program-ITT103-SP2025.py
# Point of Sale System for Best Buy Retail Store

import datetime
import time
import os

class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

# Dictionary to store items in shopping cart
class ShoppingCart:
    def __init__(self):
        self.items = {}  
        
    #method to add item to shopping cart 
    def add_item(self, product, quantity):
        if product.name in self.items:
            self.items[product.name] += quantity
        else:
            self.items[product.name] = quantity
        product.stock -= quantity
    
    #method to remove item from shopping cart 
    def remove_item(self, product, quantity):
        if product.name in self.items:
            if self.items[product.name] <= quantity:
                product.stock += self.items[product.name]
                del self.items[product.name]
            else:
                self.items[product.name] -= quantity
                product.stock += quantity

    #method to view items in cart  
    def view_cart(self, product_catalog):
        if not self.items:
            print("\nCart is empty.")
            return
        
        print("\n" + "=" * 50)
        print("SHOPPING CART".center(50))
        print("=" * 50)
        print(f"{'Item':<25}{'Qty':<10}{'Price':<10}{'Total':<10}")
        print("-" * 50)
        
        subtotal = 0
        for product_name, quantity in self.items.items():
            product = product_catalog[product_name]
            item_total = product.price * quantity
            subtotal += item_total
            print(f"{product.name[:24]:<25}{quantity:<10}${product.price:<9.2f}${item_total:<9.2f}")
        
        print("-" * 50)
        print(f"{'Subtotal:':<35}${subtotal:<9.2f}")
        print("=" * 50)

     #method to calculate total cost   
    def calculate_total(self, product_catalog):
        subtotal = 0
        for product_name, quantity in self.items.items():
            product = product_catalog[product_name]
            subtotal += product.price * quantity
        return subtotal
    
    #method to clear all items from cart
    def clear_cart(self):
        self.items.clear()

class POSSystem:
    def __init__(self):
        self.product_catalog = {}
        self.initialize_products()
        self.shopping_cart = ShoppingCart()
        self.transaction_count = 0
    
    #method that initializes list to product catalog
    def initialize_products(self):
        # Name, Price, Stock
        products = [
            ( "Milk", 500, 20),
            ( "Bread", 600, 30),
            ( "Eggs ", 560, 25),
            ( "Chicken ", 800, 20),
            ( "Rice", 200, 20),
            ( "Apples ", 100, 40),
            ( "Bananas", 1200, 32),
            ( "Cereal", 900, 25),
            ( "Coffee", 350, 18),
            ( "Toilet Paper", 200, 22),
            ( "Laundry Detergent", 1000, 12),
            ( "Dish Soap", 450, 30),
            ( "Orange Juice", 250, 30)
        ]
        
        for product in products:
            self.product_catalog[product[0]] = Product(product[0], product[1], product[2])
    
    #method to display the products in the catalog
    def display_products(self):
        print("\n" + "=" * 60)
        print("PRODUCT CATALOG".center(60))
        print("=" * 60)
        print(f"{'Product':<30}{'Price':<10}{'Stock':<10}")
        print("-" * 60)
        
        for product_name, product in self.product_catalog.items():
            # Check if stock is low
            stock_display = f"{product.stock}"
            if product.stock < 5:
                stock_display += " (YOU HAVE LESS THAN 5 REMAINING !)"
            print(f"{product.name[:29]:<30}${product.price:<9.2f}{stock_display:<10}")
        
        print("=" * 60)
    
    #method to add items to cart
    def add_to_cart(self):
        try:
            self.display_products()
            product_name = (input("\nEnter product name to add item to cart: "))
            
            if product_name not in self.product_catalog:
                print("Invalid product name")
                return
            
            product = self.product_catalog[product_name]
            
            quantity = int(input(f"Enter quantity for {product.name}: "))
            if quantity <= 0:
                print("Quantity must be positive.")
                return
            
            if quantity > product.stock:
                print(f"Insufficient stock. Only {product.stock} available.")
                return
                
            
            self.shopping_cart.add_item(product, quantity)
            print(f"{quantity} {product.name} added to cart.")
            
        except ValueError:
            print("Please enter a valid number.")
    
    #method to remove items from cart 
    def remove_from_cart(self):
        if not self.shopping_cart.items:
            print("\nCart is empty.")
            return
        
        try:
            self.shopping_cart.view_cart(self.product_catalog)
            product_name= (input("\nEnter product name to remove from cart: "))
            
            if product_name not in self.shopping_cart.items:
                print("Product is not in cart.")
                return
            
            product = self.product_catalog[product_name]
            quantity = int(input(f"Enter quantity to remove (max {self.shopping_cart.items[product_name]}): "))
            
            if quantity <= 0:
                print("Quantity must be positive.")
                return
            
            if quantity > self.shopping_cart.items[product_name]:
                print(f"Cannot remove more than {self.shopping_cart.items[product_name]} items.")
                return
            
            self.shopping_cart.remove_item(product, quantity)
            print(f"{quantity} {product.name} has been removed from cart.")
            
        except ValueError:
            print("Please enter a valid number.")
    

    def process_checkout(self):
        if not self.shopping_cart.items:
            print("\nCart is empty. Cannot checkout.")
            return
        
        subtotal = self.shopping_cart.calculate_total(self.product_catalog)
        
        # Apply discount if applicable
        discount = 0
        if subtotal > 5000:
            discount = subtotal * 0.05
            print(f"\n5% discount applied for orders over $500: -${discount:.2f}")
            
        subtotal_after_discount = subtotal - discount
        
        # Apply tax
        tax = subtotal_after_discount * 0.10
        total = subtotal_after_discount + tax
        
        # Display totals
        print("\n" + "=" * 50)
        print("CHECKOUT SUMMARY".center(50))
        print("=" * 50)
        print(f"Subtotal: ${subtotal:.2f}")
        if discount > 0:
            print(f"Discount: -${discount:.2f}")
        print(f"Tax (10%): ${tax:.2f}")
        print(f"TOTAL: ${total:.2f}")
        print("=" * 50)
        
        # Process payment
        while True:
            try:
                payment = float(input("\nEnter payment amount: $"))
                if payment < total:
                    print(f"Insufficient funds. Total amount due is: ${total:.2f}")
                    continue
                
                change = payment - total
                print(f"Change: ${change:.2f}")
                
                # Generate receipt
                self.generate_receipt(subtotal, discount, tax, total, payment, change)
                
                # Reset cart for next transaction
                self.shopping_cart.clear_cart()
                self.transaction_count += 1
                break
                
            except ValueError:
                print("Please enter a valid amount.")
    
    
    def generate_receipt(self, subtotal, discount, tax, total, payment, change):
        # Clear screen for receipt
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("\n" + "=" * 50)
        print("BEST BUY RETAIL STORE".center(50))
        print("123 Programming Techniques Street, UCC".center(50))
        print("Tel: (555) 765-4321".center(50))
        print("-" * 50)
        print(f"Date: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Transaction #: {self.transaction_count + 1}")
        print("-" * 50)
        print(f"{'Item':<25}{'Qty':<10}{'Price':<10}{'Total':<10}")
        print("-" * 50)
        
        for product_name, quantity in self.shopping_cart.items.items():
            product = self.product_catalog[product_name]
            item_total = product.price * quantity
            print(f"{product.name[:24]:<25}{quantity:<10}${product.price:<9.2f}${item_total:<9.2f}")
        
        print("-" * 50)
        print(f"{'Subtotal:':<35}${subtotal:<9.2f}")
        
        if discount > 0:
            print(f"{'Discount (5%):':<35}-${discount:<9.2f}")
            print(f"{'Subtotal after discount:':<35}${subtotal - discount:<9.2f}")
            
        print(f"{'Tax (10%):':<35}${tax:<9.2f}")
        print(f"{'TOTAL:':<35}${total:<9.2f}")
        print("-" * 50)
        print(f"{'Payment:':<35}${payment:<9.2f}")
        print(f"{'Change:':<35}${change:<9.2f}")
        print("-" * 50)
        print("Thank you for shopping at Best Buy Retail Store!".center(50))
        print("Please come again soon!".center(50))
        print("=" * 50)
        
        # Save receipt option
        input("\nPress Enter to continue...")
    
    def main_menu(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n" + "=" * 50)
            print("BEST BUY RETAIL STORE POS SYSTEM".center(50))
            print("=" * 50)
            print("1. View Products")
            print("2. Add Item to Cart")
            print("3. Remove Item from Cart")
            print("4. View Shopping Cart")
            print("5. Clear Shopping Cart")
            print("6. Checkout")
            print("7. Exit")
            print("=" * 50)
            
            choice = input("Enter your choice (1-6): ")
            
            if choice == '1':
                self.display_products()
                input("\nPress Enter to continue...")
            elif choice == '2':
                self.add_to_cart()
                input("\nPress Enter to continue...")
            elif choice == '3':
                self.remove_from_cart()
                input("\nPress Enter to continue...")
            elif choice == '4':
                self.shopping_cart.view_cart(self.product_catalog)
                input("\nPress Enter to continue...")
            elif choice == '5':
                self.shopping_cart.clear_cart()
                input("\nPress Enter to continue...")
            elif choice == '6':
                self.process_checkout()
            elif choice == '7':
                print("\nThank you for using Best Buy Retail Store POS System!")
                break
            else:
                print("\nInvalid choice. Please try again.")
                input("\nPress Enter to continue...")

# Run the POS system
pos = POSSystem()
pos.main_menu()


