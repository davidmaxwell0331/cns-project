CNS 1001 Project 2 ; Inventory & Sales Tracker

# Project Title

# Student Information
Xavier Subratie (2509139) - **Project Lead, Architecture**
Ethan Eubanks (2509775) - **Lead Developer (Core Logic)**
Rodaine Wuarrie (2409674) - **Developer (Data & Validation)**
Rajali Burrell (2007948) - **QA & Testing Lead**
Mikayliea Edwards (2403230) - **Documentation Lead**
David Maxwell (n/a) - **Presentation & Demo Lead**
(course ; CNS1001 - Introduction to Programming)

# Problem Statement 

The problem I wanted to solve is essentially how small businesss track their sales without buying expensive software. Alot of small shops typically track sales by hand, making it hard to calculate the sales averages or see what products are even selling. This simple program gives a very simple way to log products, record monthly sales as well as automatically see the performance ratings without doing much or any manual math.

# Program Description

A text-based python menu with 10 options to choose from. It stores the products in a dictionary list (SKU, holding name, nested dictionary w/ monthly sales). Users can add products, log their sales, calculate averages, search for items, view formatted tables and save or load data to a JSON file so nothing is lost whenever the program is closed.

# Programming Concepts used

Variables & I/O: Storing user inputs and printing menus.
Conditionals: Routing the menu and calculating performance ratings (Excellent, Good, Average, Low).
Loops: while True for the main menu; for loops to search data and print tables.
Functions: 11 total. Created a find_product() helper to avoid repeating search code.
Lists & Dictionaries: Main data structure (inventory_data) with nested dicts for sales.
File Handling: Using built-in json module to save/load data.
String Formatting: f-strings and padding (<15) to align table columns.
Validation & Exceptions: get_valid_input() blocks bad data; try/except handles missing save files.

# How to Run the Program
1. Open your terminal in the folder **project.py**
2. Run **python project.py**
3. Follow the **numbered menu**. Press 0 to exit.

# Required Libraries
No libraries required as python is built-in the file.

# Sample Inputs and Outputs

Logging sales and adding a product: 

Enter choice: 1Enter product name: Mechanical KeyboardEnter product SKU: KB-001Product 'Mechanical Keyboard' (SKU: KB-001) added successfully.Enter choice: 2Enter product name or SKU: KB-001Enter month (e.g., Jan, Feb): JanEnter units sold: 120Recorded 120 units sold for Jan.
