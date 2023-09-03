# ------------------------------------------------------------------------ #
# Title: Assignment 08 - Final
# Description: Working with classes

# ChangeLog (Nicole Tenev, 9-2-23, Add code to pseudo code with exception handling):
# RRoot, 1.1.2030, Created started script
# RRoot, 1.1.2030, Added pseudo-code to start assignment 8
# Nicole Tenev, 9/2/2023, Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the product's  name
        product_price: (float) with the product's standard price

    methods:
    changelog: (When, Who, What)
        RRoot, 1.1.2030, Created Class
        Nicole Tenev, 9/2/2023, Modified code to complete assignment 8
    """
    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):
        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When, Who, What)
        RRoot, 1.1.2030, Created Class
        Nicole Tenev, 9/2/2023, Modified code to complete assignment 8
    """
    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        try:
            with open(file_name, 'w') as file:
                for product in list_of_product_objects:
                    file.write(f"{product.product_name},{product.product_price}\n")
            print("Data saved to file successfully.")
        except Exception as e:
            print("An error occurred while saving data to file:", str(e))

    @staticmethod
    def read_data_from_file(file_name):
        list_of_products = []
        try:
            with open(file_name, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    data = line.strip().split(',')
                    if len(data) == 2:
                        product_name, product_price = data
                        list_of_products.append(Product(product_name, float(product_price)))
            return list_of_products
        except FileNotFoundError:
            print("File not found. No data loaded.")
            return list_of_products
        except Exception as e:
            print("An error occurred while reading data from file:", str(e))
            return list_of_products

# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """A class for performing Input and Output

    methods:
        print_menu_items():
        print_current_list_items(list_of_rows):
        input_product_data():

    changelog: (When, Who, What)
        RRoot, 1.1.2030, Created Class
    """
    # Add code to show menu to the user (Done for you as an example)
    @staticmethod
    def print_menu_items():
        """Display a menu of choices to the user"""
        print('''
        Menu of Options
        1) Show current data
        2) Add a new item
        3) Save Data to File
        4) Exit Program
        ''')

    @staticmethod
    def get_user_choice():
        """Get the user's menu choice"""
        choice = input("Enter your choice (1/2/3/4): ")
        return choice

    @staticmethod
    def print_current_list_items(list_of_rows):
        """Show the current data from the list of product objects"""
        print("\nCurrent Data:")
        for product in list_of_rows:
            print(f"Product Name: {product.product_name}, Product Price: {product.product_price}")
        print()

    @staticmethod
    def input_product_data():
        """Get product data from the user"""
        product_name = input("Enter the product name: ")
        product_price = float(input("Enter the product price: "))
        return Product(product_name, product_price)

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when the script starts
lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

while True:
    # Show the menu to the user
    IO.print_menu_items()
    user_choice = IO.get_user_choice()

    if user_choice == '1':
        # Show current data
        IO.print_current_list_items(lstOfProductObjects)
    elif user_choice == '2':
        # Add a new item
        new_product = IO.input_product_data()
        lstOfProductObjects.append(new_product)
    elif user_choice == '3':
        # Save Data to File
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
    elif user_choice == '4':
        # Exit Program
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
# Main Body of Script  ---------------------------------------------------- #


