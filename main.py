import db
import billing

def show_products():
    products = db.get_all_products()
    if not products:
        print("\nNo products found.\n")
        return
    
    print("\n==== PRODUCT LIST ====")
    for p in products:
        print(f"ID: {p[0]} | Name: {p[1]} | Price: ₹{p[2]} | Qty: {p[3]}")

        # LOW STOCK ALERT
        if p[3] < 5:
            print(f"⚠ LOW STOCK: {p[1]} — only {p[3]} left!")

    print("=======================\n")


def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))
    
    ok, msg = db.add_product(name, price, qty)
    print(msg)

def search_product():
    keyword = input("Enter product name or ID to search: ")

    results = db.search_products(keyword)

    if not results:
        print("\nNo matching products found.\n")
        return

    print("\n===== SEARCH RESULTS =====")
    for p in results:
        print(f"ID: {p[0]} | Name: {p[1]} | Price: ₹{p[2]} | Qty: {p[3]}")
    print("==========================\n")

def update_product():
    pid = int(input("Enter Product ID to update: "))
    prod = db.get_product_by_id(pid)

    if not prod:
        print("Invalid Product ID!")
        return
    
    print(f"Current Price: {prod[2]}, Current Quantity: {prod[3]}")
    
    new_price = float(input("Enter new price: "))
    new_qty = int(input("Enter new quantity: "))

    db.update_product(pid, price=new_price, quantity=new_qty)
    print("Product updated successfully.")

def delete_product():
    pid = int(input("Enter Product ID to delete: "))
    msg = db.delete_product(pid)
    print(msg)

def billing_menu():
    cart = []
    print("\nAdd items to cart. Type '0' to finish.\n")
    
    while True:
        pid = int(input("Product ID: "))
        if pid == 0:
            break
        qty = int(input("Quantity: "))
        cart.append((pid, qty))
    
    billing.generate_bill(cart)

def main():
    while True:
        print("\n===== Grocery Store Menu =====")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Billing")
        print("7. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_product()
        elif choice == "2":
            show_products()
        elif choice == "3":
            search_product()
        elif choice == "4":
            update_product()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            billing_menu()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid option! Try again.")

if __name__ == "__main__":
    main()