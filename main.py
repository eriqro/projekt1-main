import csv
import os
from text import welcome
from text import exit_text

FILENAME = 'db_inventory.csv'

def load_data(filename):
    products = []
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    "id": int(row['id']),
                    "name": row['name'],
                    "desc": row['desc'],
                    "price": float(row['price']),
                    "quantity": int(row['quantity']),
                })
    except FileNotFoundError:
        print("Inventory file not found. Starting with an empty list.")
    return products

def save_data(filename, products):
    with open(filename, 'w', newline='') as file:
        fieldnames = ['id', 'name', 'desc', 'price', 'quantity']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)

def get_product(products, product_id):
    return next((product for product in products if product['id'] == product_id), None)

def add_product(products):
    try:
        product = {
            "id": int(input("ID: ")),
            "name": input("Name: "),
            "desc": input("Description: "),
            "price": float(input("Price: ")),
            "quantity": int(input("Quantity: "))
        }
        products.append(product)
        print("Product added successfully.")
    except ValueError:
        print("Invalid input. Please try again.")

def remove_product(products):
    try:
        product_id = int(input("Enter the ID of the product to remove: "))
        product = get_product(products, product_id)
        if product:
            products.remove(product)
            print("Product removed successfully.")
        else:
            print("Product not found.")
    except ValueError:
        print("Invalid input. Please enter a valid ID.")

def edit_product(products):
    try:
        product_id = int(input("Enter the ID of the product to edit: "))
        product = get_product(products, product_id)
        if product:
            print(f"Editing Product - {product}")
            product['name'] = input("Enter new name (leave blank to keep current): ") or product['name']
            product['desc'] = input("Enter new description (leave blank to keep current): ") or product['desc']
            product['price'] = float(input("Enter new price (leave blank to keep current): ") or product['price'])
            product['quantity'] = int(input("Enter new quantity (leave blank to keep current): ") or product['quantity'])
            print("Product updated successfully.")
        else:
            print("Product not found.")
    except ValueError:
        print("Invalid input. Please try again.")

def view_products(products):
    print("\nAvailable Products:")
    if products:
        for product in products:
            print(f"ID: {product['id']}, Name: {product['name']}, Description: {product['desc']}, "
                  f"Price: {product['price']}, Quantity: {product['quantity']}")
    else:
        print("No products available.")
    print("\n")

def main():
    products = load_data(FILENAME)
    while True:
        os.system('cls')
        welcome()
        view_products(products)
        print(
            "1. Add a new product\n"
            "2. Remove an existing product\n"
            "3. Edit a product by ID\n"
            "4. Exit\n"
        )
        choice = input("Enter your choice: ")
        if choice == "1":
            add_product(products)
            save_data(FILENAME, products)
        elif choice == "2":
            remove_product(products)
            save_data(FILENAME, products)
        elif choice == "3":
            edit_product(products)
            save_data(FILENAME, products)
        elif choice == "4":
            os.system('cls')
            exit_text()
            break
        else:
            print("Invalid choice. Please try again.")
            input("\nPress Enter to continue.")

if __name__ == "__main__":
    main()