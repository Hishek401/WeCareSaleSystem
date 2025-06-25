# main.py
from read import load_products
from operations import sell_products, restock_products

def main():
    """
    Entry point of the program. Displays the main menu and allows the user
    to perform sales, restocking, or exit the program.
    """
    print("=== WECARE WHOLESALE SYSTEM ===")
    products = load_products()

    while True:
        print("\nMain Menu")
        print("1. Sell Products")
        print("2. Restock Products")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            sell_products(products)
        elif choice == "2":
            restock_products(products)
        elif choice == "3":
            print("Thank you for using WeCare!")
            break
        else:
            print("Invalid choice.")

main()
