# CNS1001 Project 2: Inventory & Sales Tracker

## (a) Project Title
Inventory & Sales Tracker

## (b) Student Information
| Name | ID | Role |
|---|---|---|
| Xavier Subratie | 2509139 | Project Lead |
| Ethan Eubanks | 2509775 | Lead Developer |
| Rodaine Wuarrie | 2409674 | Developer (Data & Validation) |
| Rajali Burrell | 2007948 | QA & Testing Lead |
| Mikayliea Edwards | 2403230 | Documentation Lead |
| David Maxwell | 2409061 | Presentation Lead |

(course ; CNS1001 - Introduction to Programming)

## (c) Problem Statement 

The problem I wanted to solve is essentially how small businesss track their sales without buying expensive software. Alot of small shops typically track sales by hand, making it hard to calculate the sales averages or see what products are even selling. This simple program gives a very simple way to log products, record monthly sales as well as automatically see the performance ratings without doing much or any manual math.

## (d) Program Description

A text-based python menu with 10 options to choose from. It stores the products in a dictionary list (SKU, holding name, nested dictionary w/ monthly sales). Users can add products, log their sales, calculate averages, search for items, view formatted tables and save or load data to a JSON file so nothing is lost whenever the program is closed.

## (e) Programming Concepts used

Variables & I/O: Storing user inputs and printing menus.
Conditionals: Routing the menu and calculating performance ratings (Excellent, Good, Average, Low).
Loops: while True for the main menu; for loops to search data and print tables.
Functions: 11 total. Created a find_product() helper to avoid repeating search code.
Lists & Dictionaries: Main data structure (inventory_data) with nested dicts for sales.
File Handling: Using built-in json module to save/load data.
String Formatting: f-strings and padding (<15) to align table columns.
Validation & Exceptions: get_valid_input() blocks bad data; try/except handles missing save files.

## (f) How to Run the Program
1. Open your terminal in the folder **project.py**
2. Run **python project.py**
3. Follow the **numbered menu**. Press 0 to exit.

## (g) Required Libraries
No libraries required, python built-in.

## (h) Sample Inputs and Outputs

**Adding a product and logging sales:**
```text
Enter choice: 1
Enter product name: Keyboard
Enter product SKU: KB-001
Product 'Keyboard' (SKU: KB-001) added successfully.

Enter choice: 2
Enter product name or SKU: KB-001
Enter month (e.g., Jan, Feb): Jan
Enter units sold: 120
Recorded 120 units sold for Jan.
```

**Viewing the full inventory table:**
```text
Enter choice: 5
======= Full Warehouse View =======
Product         | SKU      | Avg Sales     | Status
----------------------------------------------------
Keyboard        | KB-001   | 120.00        | Excellent
----------------------------------------------------
Total Items: 1 | Store Average: 120.00
======================================
```

## (i) Manual Testing / Validation

| Test Case | Input | Expected Output | Actual Output | Pass/Fail |
|---|---|---|---|---|
| Add new product | Choice: 1, Name: Mouse, SKU: M-01 | Product added successfully | Product 'Mouse' (SKU: M-01) added successfully. | Pass |
| Duplicate SKU | Choice: 1, SKU: M-01 again | Error message | Error: A product with SKU 'M-01' already exists. | Pass |
| Negative sales input | Choice: 2, Units: -5 | Validation error | Value must be at least 0. | Pass |
| Invalid menu choice | Choice: abc | Error message | Invalid option. Please enter a number from the menu. | Pass |
| Load with no save file | Choice: 9 (no file exists) | Graceful failure message | No saved data found. | Pass |

## (j) Challenges and Lessons Learned
**Challenge 1:** The product search loop was duplicated across multiple functions, making the code difficult to maintain.

**our fix;** We extracted it into a single `find_product()` helper that every function now calls.

**Challenge 2:** `load_data()` wasn't updating the main inventory after loading from file.

**our fix;** We added `global inventory_data` inside the function. Without it, Python would be treating the assignment as a new local variable and the main list stays empty.

**Lesson:** small structural decisions early on need to be used, saves significant cleanup time.

## (k) AI Assistance Disclosure
**Tool used:** Claude (Anthropic)
**Purpose:** Debugging the `global` variable issue in `load_data()`, understanding Python string padding for table formatting, and syntax clarification.
**Validation:** All suggestions were tested manually and understood before being included. All code was written and verified by the group.