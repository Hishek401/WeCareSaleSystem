# write.py
#new branch crated 
#Hishek Yonjan
from datetime import datetime

def save_products(products, filename="inventory.txt"):
    """
    Saves the current product data to the inventory file.

    Parameters:
    products (dict): Dictionary containing all product information.
    filename (str): Name of the file where the products will be saved.
    """
    try:
        file = open(filename, "w")
        for p in products.values():
            line = p["name"] + "," + p["brand"] + "," + str(p["stock"]) + "," + str(p["cost_price"]) + "," + p["origin"] + "\n"
            file.write(line)
        file.close()
    except Exception as e:
        print("Error saving products:", e)

def generate_invoice(invoice_type, details, items):
    """
    Generates a sale or restock invoice, prints it to the terminal, and saves it to a text file.

    Parameters:
    invoice_type (str): Either 'sales' or 'restock'.
    details (dict): Customer or supplier information along with total amount.
    items (list): List of items involved in the transaction.
    """
    try:
        now = datetime.now()
        timestamp = str(now.year) + "-" + str(now.month) + "-" + str(now.day) + "_" + str(now.hour) + "-" + str(now.minute)
        filename = invoice_type + "_invoice_" + timestamp + ".txt"

        file = open(filename, "w")
        invoice_lines = []
        invoice_lines.append("=== WeCare Wholesale ===")
        if invoice_type == "sales":
            invoice_lines.append("Invoice Type: SALE")
            invoice_lines.append("Customer: " + details["name"])
            invoice_lines.append("Phone: " + str(details["phone"]))
        else:
            invoice_lines.append("Invoice Type: RESTOCK")
            invoice_lines.append("Supplier: " + details["name"])
        invoice_lines.append("Date: " + timestamp)
        invoice_lines.append("----------------------------------------")

        for item in items:
            if invoice_type == "sales":
                invoice_lines.append(item["name"] + " (" + item["brand"] + ") - Qty: " + str(item["qty"]) + " (+ " + str(item["free"]) + " free) - Rs" + str(item["price"] * item["qty"]))
            else:
                invoice_lines.append(item["name"] + " (" + item["brand"] + ") - Qty: " + str(item["qty"]) + " - Cost: Rs" + str(item["cost_price"]))

        invoice_lines.append("----------------------------------------")
        invoice_lines.append("TOTAL: Rs" + str(details["total"]))

        for line in invoice_lines:
            print(line)
            file.write(line + "\n")

        file.close()
        print("Invoice saved as '" + filename + "'")
    except Exception as e:
        print("Error generating invoice:", e)
