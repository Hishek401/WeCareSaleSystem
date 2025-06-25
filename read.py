# read.py

def load_products(filename="inventory.txt"):
    """
    Loads product data from the inventory file into a dictionary.

    Parameters:
    filename (str): The name of the inventory file to load from.

    Returns:
    dict: A dictionary of products, with keys as product IDs and values as product details.
    """
    products = {}
    try:
        file = open(filename, "r")
        for line in file:
            if line != "\n":
                parts = line.split(",")
                if len(parts) == 5:
                    product_id = len(products) + 1
                    products[product_id] = {
                        "name": parts[0],
                        "brand": parts[1],
                        "stock": int(parts[2]),
                        "cost_price": int(parts[3]),
                        "origin": parts[4].strip()
                    }
        file.close()
    except FileNotFoundError:
        print("Note: 'inventory.txt' not found. Starting with empty inventory.")
    except Exception as e:
        print("Error loading products:", e)
    return products
