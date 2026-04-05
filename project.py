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
    
    # Check if SKU already exists
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
    product_found = None
    
    for product in inventory_data:
        if search_term.lower() == product["name"].lower() or search_term == product["sku"]:
            product_found = product
            break
            
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
    
def main():
    """the main loop of the program"""
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
            if not inventory_data:
                print("No products found. Please add a product first.")
            else:
                search = get_valid_input("Enter product name or SKU: ")
                found = None
                for product in inventory_data:
                    if search.lower() == product["name"].lower() or search == product["sku"]:
                        found = product
                        break
                if found:
                    avg = calculate_average(found)
                    print(f"{found['name']}'s Average Monthly Sales: {avg:.2f} units")
                else:
                    print(f"Product '{search}' not found.")
        else:
            print(f"Option {choice} is not yet implemented.")

if __name__ == "__main__":
    main()