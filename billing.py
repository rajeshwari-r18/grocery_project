import db

def generate_bill(cart):
    total = 0
    print("\n===== BILL =====")
    for pid, qty in cart:
        product = db.get_product_by_id(pid)
        if product:
            name = product[1]
            price = product[2]
            amount = price * qty
            total += amount
            print(f"{name}  x{qty}  = ₹{amount}")
            
            # reduce stock
            new_qty = product[3] - qty
            db.update_product(pid, quantity=new_qty)
        else:
            print(f"Product ID {pid} not found!")

    print("--------------------")
    print(f"TOTAL BILL = ₹{total}")
    print("====================\n")

    return total