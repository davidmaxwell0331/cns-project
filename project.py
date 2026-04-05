# CNS1001 - Introduction to Programming
# Project 2
# inventory & sales tracker
# members : Xavier Subratie   (2509139) - project lead, architecture
#           Ethan Eubanks     (2509775) - lead dev (core logic)
#           Rodaine Wuarrie   (2409674) - dev (data & validation)
#           Rajali Burrell    (2007948) - QA & Testing lead
#           Mikayliea Edwards (2403230) - documentation lead
#           David Maxwell     (insert your id here, david) - presentation & demo lead

# main data structure ~ holds everything, list of dictionaries.
# format: [{"name": "Keyboard", "sku": "KB-001", "sales": {"Jan": 50, "Feb": 65}}]
inventory_data = []

def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- Inventory & Sales Tracker ---")
    print("1. Add Product")
    print("2. Add Monthly Sales")
    print("3. Calculate Average Sales")
    print("4. Product Report")
    print("5. Full Inventory Report")
    print("6. Search Product")
    print("7. Inventory Summary")
    print("8. Save Data")
    print("9. Load Data")
    print("0. Exit")

def get_valid_input(prompt, input_type="str", min_val=None, max_val=None):
    """
    Validates user input based on type and range.
    input_type: 'str' for text, 'int' or 'float' for numbers
    """
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Input cannot be empty. Please try again.")
            continue
        
        if input_type == "str":
            return user_input
        elif input_type in ("int", "float"):
            try:
                value = float(user_input) 
                if input_type == "int" and not user_input.isdigit() and not (user_input.startswith('-') and user_input[1:].isdigit()):
                    raise ValueError 
                if min_val is not None and value < min_val:
                    print(f"Value must be at least {min_val}.")
                    continue
                if max_val is not None and value > max_val:
                    print(f"Value must be at most {max_val}.")
                    continue
                return int(value) if input_type == "int" else value
            except ValueError:
                print("Invalid input. Please enter a valid number.")

def add_product():
    """Adds a new product to the inventory_data list."""
    print("\n--- Add New Product ---")
    name = get_valid_input("Enter product name: ")
    sku = str(get_valid_input("Enter product SKU: "))
    
    # checks if sku already exists
    for product in inventory_data:
        if product["sku"] == sku:
            print(f"Error: A product with SKU '{sku}' already exists.")
            return
            
    new_product = {
        "name": name,
        "sku": sku,
        "sales": {}
    }
    inventory_data.append(new_product)
    print(f"Product '{name}' (SKU: {sku}) added successfully.")

def add_monthly_sales():
    """Adds or updates sales figures for an existing product."""
    print("\n--- Add Monthly Sales ---")
    if not inventory_data:
        print("No products found. Please add a product first.")
        return
    
    search_term = get_valid_input("Enter product name or SKU: ")
    product_found = find_product(search_term)
            
    if not product_found:
        print(f"Product '{search_term}' not found.")
        return
        
    month = get_valid_input("Enter month (e.g., Jan, Feb): ")
    # validation: can't sell negative items
    units = get_valid_input("Enter units sold: ", input_type="int", min_val=0)
    
    product_found["sales"][month] = units
    print(f"Recorded {units} units sold for {month}.")

def calculate_average(product):
    """Calculates the average monthly sales of a product."""
    sales = product["sales"]
    if not sales:
        return 0.0
    return sum(sales.values()) / len(sales)

def get_performance_rating(average):
    """Converts average sales to a performance rating."""
    if average >= 100:
        return "Excellent"
    elif average >= 50:
        return "Good"
    elif average >= 20:
        return "Average"
    else:
        return "Low"

def show_product_stats():
    """pulls up the full breakdown for one specific item"""
    print("\n--- Item Lookup ---")
    if len(inventory_data) == 0:
        print("Nothing in the system yet. Go back and add stuff.")
        return
        
    search = get_valid_input("Enter product name or SKU: ")
    matched_item = find_product(search)
            
    if matched_item is None:
        print(f"Couldn't find '{search}' in the inventory.")
        return
        
    print(f"\n======= Item Breakdown =======")
    print(f"Product: {matched_item['name']}")
    print(f"SKU:     {matched_item['sku']}")
    print("-" * 28)
    
    if not matched_item["sales"]:
        print("No sales recorded for this yet.")
    else:
        for month, units in matched_item["sales"].items():
            print(f"{month:<10}: {units} sold")
        print("-" * 28)
        avg = calculate_average(matched_item)
        rating = get_performance_rating(avg)
        print(f"Avg Sales: {avg:.2f} units -> Rating: {rating}")
    print("=" * 28)

def show_full_inventory():
    """prints out the big table of everything we have"""
    print("\n======= Full Warehouse View =======")
    if len(inventory_data) == 0:
        print("Inventory is totally empty.")
        return
        
    # setting up the table headers
    print(f"{'Product':<15} | {'SKU':<8} | {'Avg Sales':<12} | {'Status'}")
    print("-" * 52)
    
    running_total = 0
    for item in inventory_data:
        avg = calculate_average(item)
        running_total += avg
        rating = get_performance_rating(avg)
        # the <15 and <8 spaces things out so it looks like a table
        print(f"{item['name']:<15} | {item['sku']:<8} | {avg:<12.2f} | {rating}")
        
    print("-" * 52)
    overall_avg = running_total / len(inventory_data)
    print(f"Total Items: {len(inventory_data)} | Store Average: {overall_avg:.2f}")
    print("=" * 38)

def find_product(search_term):
    """Finds and returns a product by name or SKU, or None if not found."""
    for product in inventory_data:
        if search_term.lower() == product["name"].lower() or search_term == product["sku"]:
            return product
    return None

def calculate_average_sales():
    """Asks for a product and prints its average monthly sales."""
    print("\n--- Calculate Average Sales ---")
    if not inventory_data:
        print("No products found. Please add a product first.")
        return
    search = get_valid_input("Enter product name or SKU: ")
    found = find_product(search)
    if found:
        avg = calculate_average(found)
        print(f"{found['name']}'s Average Monthly Sales: {avg:.2f} units")
    else:
        print(f"Product '{search}' not found.")

def search_product():
    """Searches for a product and shows its info."""
    print("\n--- Search Product ---")
    search = get_valid_input("Enter product name or SKU: ")
    product = find_product(search)
    if product:
        print(f"Found: {product['name']} | SKU: {product['sku']} | Sales: {product['sales']}")
    else:
        print(f"Product '{search}' not found.")

def inventory_summary():
    """Prints a quick summary of all products."""
    print("\n--- Inventory Summary ---")
    if not inventory_data:
        print("No products found.")
        return
    print(f"Total products: {len(inventory_data)}")
    for product in inventory_data:
        avg = calculate_average(product)
        print(f"  - {product['name']} (SKU: {product['sku']}) | Avg Sales: {avg:.2f}")

def save_data():
    """Saves inventory data to a file."""
    import json
    with open("inventory.json", "w") as f:
        json.dump(inventory_data, f)
    print("Data saved to inventory.json")

def load_data():
    """Loads inventory data from a file."""
    import json
    global inventory_data
    try:
        with open("inventory.json", "r") as f:
            inventory_data = json.load(f)
        print(f"Loaded {len(inventory_data)} product(s).")
    except FileNotFoundError:
        print("No saved data found.")

def main():
    """The main loop of the program."""
    print("Welcome to the Inventory & Sales Tracker!")

    while True:
        display_menu()
        choice = input("Enter choice: ")

        if choice == '0':
            print("Exiting program. Goodbye!")
            break
        elif choice == '1':
            add_product()
        elif choice == '2':
            add_monthly_sales()
        elif choice == '3':
            calculate_average_sales()
        elif choice == '4':
            show_product_stats()
        elif choice == '5':
            show_full_inventory()
        elif choice == '6':
            search_product()
        elif choice == '7':
            inventory_summary()
        elif choice == '8':
            save_data()
        elif choice == '9':
            load_data()
        else:
            print("Invalid option. Please enter a number from the menu.")

if __name__ == "__main__":
    main()