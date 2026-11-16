#setup
import os
FILE_NAME = "products.txt"
FIRST_ID_NUMBER = 101

#Product Data
products = []    #saare products yaha rakhange(list of dictionaries)
cart = {}        #cart yaha rahega (dictionary)

#Helper functions 
def format_number(number):
    """show 50000.0 as 50000, but keep 99.5 as 99.5."""
    if float(number).is_integer():
        return str(int(number))
    return str(number)

def find_product(product_id):
    """Return the product dictionary for the given ID, or None."""
    for p in products:
        if p["id"].strip().lower() == product_id.strip().lower():
            return p
    return None

def next_product_id():
    """Generate next ID: P101 for first product, them P102, P103..."""
    if not products:
        return "p" + str(FIRST_ID_NUMBER)
    biggest = max(int(p["id"][1:]) for p in products)
    return "p" + str(biggest + 1)

def read_price(text):
    """Convert text to a positive number.Return None if invalid."""
    try:
        value = float(text)
    except ValueError:
        return None
    if value <= 0:
        return None
    return int(value) if value.is_integer() else value

def read_stock(text):
    """Convert text to a whole number >= 0.Return None if invalid."""
    try:
        value = int(text)
    except ValueError:
        return None
    if value < 0:
        return None
    return value

def show_product_line(p):
    print("ID: " + p["id"] + "| " + p["name"] + "| Price: " + format_number(p["price"]) + " | stock: " + str(p["stock"]))


#File Handling
def load_product():
    """Load products from products.txt at program start."""
    products.clear()
    if not os.path.exists(FILE_NAME):
        return
    with open(FILE_NAME, "r") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            parts = line .split(",")
            if len(parts) != 4:
                continue
            pid, name, price, stock = parts
            products.append({
                "id": pid,
                "name": name,
                "price": read_price(price) or 0,
                "stock": read_stock(stock) or 0,
            })

def save_products():
    """Save all products to products.txt (called after every change)."""  
    with open(FILE_NAME, "w") as f:
        for p in products:
            f.write(str(p["id"]) + "," + str(p["name"]) + "," + str(format_number(p["price"])) + "," + str(p["stock"]) + "\n")  


#Admin functions (CRUD)
def add_products():
    name = input("Enter product name: ").strip()
    if name == "" or "," in name:
        print("Invalid name. Name cannot be empty or contain a comma.")
        return
    
    price = read_price(input("Enter price: ").strip())
    if price is None:
        print("Invalid price. Price must be a positive number.")
        return
    stock = read_stock(input("Enter stock: ").strip())
    if stock is None:
        print("Invalid stock. Stock must be 0 or a positive whole number.")
        return

    product = {"id": next_product_id(), "name": name, "price": price, "stock": stock}
    products.append(product)
    save_products()

    if stock == 0:
        print("Product added.ID: " + product["id"] + " | " + name + " | Price " + format_number(price) + " | Stock: " + str(stock))
        print("Warning " + name + " is out of stock.")
    else:
        print("Product added.")
        show_product_line(product)

def view_products():
    if not products:
        print("No products available.")
        return
    print("-" * 50)
    for p in products:
        show_product_line(p)
    print("-" * 50)

def update_product():
    pid = input("Enter product Id to update: ").strip().upper()
    p = find_product(pid)
    if p is None:
        print("Product " + pid + " not found.")
        return

    print("Press Enter to keep the old value.")
    new_name = input("New name (" + p["name"] +"): ").strip()
    new_price = input("New price (" +format_number(p["price"]) + "): ").strip()
    new_stock = input("New stock (" + str(p["stock"]) + "): ").strip()

    if new_price !=  "":
        if "," in new_name:
            print("Invalid name.Name cannot contain a comma.")
            return
        p["name"] = new_name

    if new_price != "":
        price = read_price(new_price)
        if price is None:
            print("Invalid price.Price must be a positive number.")
            return
        p["price"] = price

    if new_stock != "":
        stock = read_stock(new_stock)
        if stock is None:
            print("Invalide stock.Stock must be 0 or a positive whole number")
            return
        p["stock"] = stock

    save_products()
    print("product update.")
    show_product_line(p)

def delete_product():
    pid = input("Enter product ID to delete: ").strip().upper()
    p = find_product(pid)
    if p is None:
        print("Product " + pid + " not found.")
        return

    products.remove(p)
    if pid in cart:
        del cart[pid]
        save_products()
        print("Product '" + p["name"] + "' deleted.Products lefts: " + str(len(products)))


#Customer functions
def add_to_cart():
    pid = input("Enter product ID: ").strip().lower()
    p = find_product(pid)
    if p is None:
        print("Product " + pid +" not found.")
        return

    try:
        qty = int(input("Enter quantity: ").strip())
    except ValueError:
        print("Invalid quantity.Enter a whole number.")
        return
    if qty <= 0:
        print("Invalid quantity.Quantity must be at least 1.")
        return

    already = cart.get(pid, 0)
    if already + qty > p["stock"]:
        print("Not enough stock.Only " + str(p["stock"]) + "available for " + p["name"] + ".")
        return

    cart[pid] = already + qty
    print(p["name"] + " x" + str(qty) + " added | Amount: " + format_number(p["price"] * qty))

def view_cart():
    if not cart:
        print("Cart is empty.")
        return
    total = 0
    for pid, qty in cart.items():
        p = find_product(pid)
        amount = p["price"] * qty
        total += amount
        print(p["name"] + " x" + str(qty) + " = " + format_number(amount))
    print("Cart total: " + format_number(total))


def checkout():
    if not cart:
        print("Cart is empty. Nothing to checkout.")
        return
 
    for pid, qty in cart.items():
        p = find_product(pid)
        if p is None or qty > p["stock"]:
            print("Stock changed. Please review your cart.")
            return
 
    total = 0
    left_info = []
    for pid, qty in cart.items():
        p = find_product(pid)
        p["stock"] -= qty                      
        total += p["price"] * qty
        left_info.append(p["name"] + " stock left: " + str(p["stock"]))
 
    cart.clear()
    save_products()
    print("Order total: " + format_number(total) + " | " + ", ".join(left_info))

#Main Menu
def show_menu():
    print("\n===== MINI E-COMMERCE SYSTEM =====")
    print("--- Admin ---")
    print("1. Add product")
    print("2. Update product")
    print("3. Delete product")
    print("4. View products")
    print("--- Customer ---")
    print("5. Add to cart")
    print("6. View cart")
    print("7. Checkout")
    print("8. Exit")
 
 
def main():
    load_product()
    while True:
        show_menu()
        choice = input("Enter your choice (1-8): ").strip()
 
        if choice == "1":
            add_products()
        elif choice == "2":
            update_product()
        elif choice == "3":
            delete_product()
        elif choice == "4":
            view_products()
        elif choice == "5":
            add_to_cart()
        elif choice == "6":
            view_cart()
        elif choice == "7":
            checkout()
        elif choice == "8":
            print("Thank you! Goodbye.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")
 
 
if __name__ == "__main__":
    main()