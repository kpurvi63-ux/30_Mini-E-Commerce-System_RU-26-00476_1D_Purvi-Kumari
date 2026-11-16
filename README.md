# Mini-E-Commerce-System
Python based Mini E-Commerce System Project

**PS No.:** 30 | **Language:** Python 3 | **Concepts:** Products, Shopping Cart, CRUD Operations, File Handling

## Author
* **Name:** Purvi Kumari
* **ERP ID:** RU-26-00476
* **Course:** B.Tech CSE (Cybersecurity)
* **College:** Rungta International Skill University
* **Project:** Mini E-Commerce System (PS No. 30)
* **Language:** Python 3
  
# About the Project
The Mini E-Commerce System is a simple shopping application developed using Python. It works through a console menu and allows users to perform basic shopping activities.

In this project, an admin can add new products, update product details, delete products, and view all available products. A Customers can add products to their cart, check their cart, and complete the checkout process.

All product details are stored in a text file named `products.txt`. This helps to save the data even after the program is closed.

# Problem Statement
The main aim of this project is to create a simple console-based shopping system where an admin can manage products and customers can purchase them.

* The system stores product information such as Product ID, Name, Price, and Stock in a file named `products.txt`.
* The first product ID starts from `P101`.
* Whenever a customer completes the checkout process, the available product stock is automatically updated.

# Features
The project includes the following features:
* **Add Product:** Add new products with an automatically generated Product ID (`P101`, `P102`, `P103`...).
* **Update Product:** Change the product name, price, or stock.
* **Delete Product:** Remove a product from the system.
* **View Products:** Display all available products with their details.
* **Add to Cart:** Add products to the shopping cart.
* **View Cart:** Check the products and their quantities in the cart.
* **Checkout:** Calculate the total amount and update the remaining stock.
* **Input Validation:** Check incorrect values entered by the user.
* **File Handling:** Save and load product information using `products.txt`.

# How the Project Works
This project uses basic Python concepts to manage products and shopping activities:
* **List of Dictionaries:** All product details are stored in a list of dictionaries.  
  *Example:* `{"id": "P101", "name": "Laptop", "price": 50000, "stock": 5}`
* **Dictionary:** The shopping cart stores Product IDs and their quantities.  
  *Example:* `{product_id: quantity}`
* **Functions:** Different functions are used to perform different operations, such as:
  * `add_product()`
  * `update_product()`
  * `delete_product()`
  * `view_products()`
  * `add_to_cart()`
  * `view_cart()`
  * `checkout()`
* **File Handling:** The `load_products()` function reads product details when the program starts, and `save_products()` saves updated details into the file.

# File Format (`products.txt`)
Product information is stored in a text file. Each product is saved on a separate line, and the values are separated by commas.

**Format:** `Product ID, Product Name, Price, Stock`

**Example:**
```text
P101,Laptop,50000,5
P102,Pen,10,100
