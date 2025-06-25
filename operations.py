# operations.py
from write import generate_invoice, save_products
from read import load_products

def display_products(products, for_sale=True):
    """
    Displays the list of products in a formatted table view.

    Parameters:
    products (dict): Dictionary of product information.
    for_sale (bool): If True, displays sale price; otherwise, shows cost price.
    """
    print("\nAvailable Products:")
    print("---------------------------------------------------------------------------")
    print("ID   Name                Brand           Stock     Price(Rs)   Origin")
    print("---------------------------------------------------------------------------")

    for pid in products:
        p = products[pid]
        price = p["cost_price"] * 2 if for_sale else p["cost_price"]

        pid_str = str(pid)
        while len(pid_str) < 5:
            pid_str += " "

        name_str = p["name"]
        while len(name_str) < 21:
            name_str += " "

        brand_str = p["brand"]
        while len(brand_str) < 17:
            brand_str += " "

        stock_str = str(p["stock"])
        while len(stock_str) < 8:
            stock_str += " "

        price_str = str(price)
        while len(price_str) < 11:
            price_str += " "

        origin_str = p["origin"]

        line = pid_str + name_str + brand_str + stock_str + price_str + origin_str
        print(line)

    print("---------------------------------------------------------------------------")

def sell_products(products):
    """
    Handles the selling process by allowing the user to input customer details,
    select products, and generate a sales invoice.

    Parameters:
    products (dict): Dictionary of current inventory items.
    """
    print("=== SELL PRODUCTS ===")
    try:
        name = input("Customer Name: ")
        while name == "":
            print("Name cannot be empty.")
            name = input("Customer Name: ")

        phone = input("Phone Number: ")
        while not phone.isdigit():
            print("Phone must be numeric.")
            phone = input("Phone Number: ")
        phone = int(phone)

        items = []
        total = 0

        while True:
            display_products(products, True)
            pid_input = input("Enter Product ID (0 to finish): ")
            if pid_input.isdigit():
                pid = int(pid_input)
            else:
                print("Invalid input.")
                continue

            if pid == 0:
                break

            if pid not in products:
                print("Invalid Product ID.")
                continue

            qty_input = input("Enter quantity: ")
            if qty_input.isdigit():
                qty = int(qty_input)
            else:
                print("Invalid quantity.")
                continue

            if qty <= 0:
                print("Quantity must be positive.")
                continue

            free = qty // 3
            total_qty = qty + free

            if total_qty > products[pid]["stock"]:
                print("Only " + str(products[pid]["stock"]) + " in stock.")
                continue

            price = products[pid]["cost_price"] * 2
            total += qty * price
            products[pid]["stock"] -= total_qty

            items.append({
                "name": products[pid]["name"],
                "brand": products[pid]["brand"],
                "qty": qty,
                "free": free,
                "price": price
            })

            print("Added " + str(qty) + " (+ " + str(free) + " free).")

            more = input("Do you want to buy more? (y/n): ")
            if more.lower() != 'y':
                break

        if items:
            generate_invoice("sales", {"name": name, "phone": phone, "total": total}, items)
            save_products(products)
        else:
            print("No products sold.")
    except Exception as e:
        print("Error during selling process:", e)

def restock_products(products):
    """
    Handles the restocking process by taking supplier details,
    updating product quantities, and generating a restock invoice.

    Parameters:
    products (dict): Dictionary of current inventory items.
    """
    print("=== RESTOCK PRODUCTS ===")
    try:
        name = input("Supplier Name: ")
        while name == "":
            print("Name cannot be empty.")
            name = input("Supplier Name: ")

        items = []
        total = 0

        while True:
            display_products(products, False)
            pid_input = input("Enter Product ID (0 to finish): ")
            if pid_input.isdigit():
                pid = int(pid_input)
            else:
                print("Invalid input.")
                continue

            if pid == 0:
                break

            if pid not in products:
                print("Invalid Product ID.")
                continue

            qty_input = input("Enter restock quantity: ")
            if qty_input.isdigit():
                qty = int(qty_input)
            else:
                print("Invalid quantity.")
                continue

            if qty <= 0:
                print("Quantity must be positive.")
                continue

            cost_input = input("Enter new cost price: ")
            if cost_input.isdigit():
                cost = int(cost_input)
            else:
                print("Invalid cost.")
                continue

            if cost <= 0:
                print("Cost must be positive.")
                continue

            products[pid]["stock"] += qty
            products[pid]["cost_price"] = cost
            total += qty * cost

            items.append({
                "name": products[pid]["name"],
                "brand": products[pid]["brand"],
                "qty": qty,
                "cost_price": cost
            })

            print("Restocked " + str(qty) + " units.")

            more = input("Do you want to restock more? (y/n): ")
            if more.lower() != 'y':
                break

        if items:
            generate_invoice("restock", {"name": name, "total": total}, items)
            save_products(products)
        else:
            print("No products restocked.")
    except Exception as e:
        print("Error during restock process:", e)
