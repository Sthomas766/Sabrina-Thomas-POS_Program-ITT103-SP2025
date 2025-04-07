# Sabrina-Thomas-POS_Program-ITT103-SP2025 

Author: Sabrina Thomas
Date Created: April 5, 2025
Course: ITT103, Programming Techniques
Github Public URL to Code:  https://github.com/Sthomas766/Sabrina-Thomas-POS_Program-ITT103-SP2025
 
REPORT
 Purpose of the Program:

This program implements a Point of Sale (POS) System for Best Buy Retail Store.
It allows users to:
 - View available products and their stock levels.
 - Add items to a shopping cart.
 - Remove items from the shopping cart.
 - View the shopping cart and subtotal.
 - Clear the shopping cart.
 - Process checkout, applying a discount for orders over $5000 and a 10% tax.
 - Generate and display a detailed receipt at checkout.

 ====================================================================================
 How to Run the Program:
 ------------------------------------------------------------------------------------
 1. Ensure Python 3.x is installed on your system.
 2. Save this file 
 3. Open a terminal or command prompt.
 4. Navigate to the directory where the file is saved.
 5. Run the program 

 The main menu will appear with options to interact with the POS system.

 ====================================================================================
 Required Modifications:
 ------------------------------------------------------------------------------------
 - Product Catalog: Update product names, prices, and stock as necessary by modifying 
   the 'initialize_products' method.
 - Tax Rate and Discount: Adjust the tax rate or discount percentage if the business 
   policies change (located in 'process_checkout' method).
 - Receipt Details: Update the store name, address, and telephone number in 
   the 'generate_receipt' method if needed.
 - Payment Validation: Currently accepts numerical payment input; enhancements 
   like credit card simulations could be added.
 - Save Receipts to File: Optionally, receipts could be saved to text files for records.

 ====================================================================================
 Assumptions and Limitations:
 ------------------------------------------------------------------------------------
 - The product names entered by the user must match exactly as shown (case-sensitive).
 - The program assumes a customer purchases and pays in one transaction at a time.
 - No multi-currency support; all prices are assumed in the same currency (JMD or USD).
 - There is no user authentication or manager override built-in.
 - Stock levels are managed per session and do not persist after the program closes.
 - Error handling is limited to basic input validation (e.g., non-numeric entries).
 - No integration with a real payment gateway; payment is simulated via user input.
 ==================================================================================== 
