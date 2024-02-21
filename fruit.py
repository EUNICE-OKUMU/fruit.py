inventory = {
    "mango": 10,
    "banana": 6,
    "apple": 11,
    "orange": 20,
    "pear": 5
}

def add_item(item, quantity):
    """Adds the specified quantity of an item to the inventory, handling updates.

    Args:
        item (str): The name of the item to add or update.
        quantity (int): The quantity to add or update.

    Raises:
        ValueError: If the quantity is not a valid positive integer.
    """
    if not isinstance(quantity, int) or quantity <= 0:
        raise ValueError("Quantity must be a positive integer.")
    inventory[item.lower()] = inventory.get(item.lower(), 0) + quantity
    print(f"Updated {item} quantity to {inventory[item]}.")

def get_item_quantity(item):
    """Returns the quantity of the specified item in the inventory.

    Args:
        item (str): The name of the item to check.

    Returns:
        int: The quantity of the item, or 0 if not found.
    """
    return inventory.get(item.lower(), 0)

def total_quantity():
    """Calculates and returns the total quantity of all items in the inventory.

    Returns:
        int: The total quantity of all items.
    """
    return sum(inventory.values())

def list_inventory():
    """Prints the inventory with quantities for each item."""
    for item, quantity in inventory.items():
        print(f"{item.title()}: {quantity}")

while True:
    print("\nInventory System:")
    print("1. Add item")
    print("2. Check item quantity")
    print("3. Show all items")
    print("4. Total items")
    print("5. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            item = input("Enter item name: ").lower()
            quantity = int(input("Enter quantity: "))
            add_item(item, quantity)
        elif choice == "2":
            item = input("Enter item name: ").lower()
            quantity = get_item_quantity(item)
            if quantity:
                print(f"{item.title()} quantity: {quantity}")
            else:
                print(f"Item '{item}' not found in inventory.")
        elif choice == "3":
            list_inventory()
        elif choice == "4":
            total = total_quantity()
            print(f"Total items: {total}")
        elif choice == "5":
            print("Exiting inventory system...")
            break
        else:
            print("Invalid choice. Please try again.")
    except ValueError as e:
        print(f"Error: {e}")

