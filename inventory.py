# Q1 - Inventory

inventory = {
    "Laptop": {"price": 899.99, "quantity": 4},
    "Keyboard": {"price": 49.99, "quantity": 12},
    "Mouse": {"price": 24.99, "quantity": 3},
    "Monitor": {"price": 199.99, "quantity": 7},
    "Headphones": {"price": 79.99, "quantity": 2}
}


def check_low_stock(threshold):
    """Print each item whose quantity is below the given threshold."""
    print(f"Items with stock below {threshold}:")

    for item, details in inventory.items():
        if details["quantity"] < threshold:
            print(f"{item}: {details['quantity']} in stock")


if __name__ == "__main__":
    check_low_stock(5)
