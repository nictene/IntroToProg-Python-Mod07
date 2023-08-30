# .....................................#
# Title: Exception Handling and Pickling
# Desc: This script demonstrates basic error handling and pickling
# Change Log: (Nicole Tenev, 8-29-2023)
# NTenev,  08-29-2023, Created File
# .....................................#

import pickle

# Data -------------------------------------------- #
user_data = {'username': 'nicole', 'team': 'msft teams'}


# Processing -------------------------------------- #

def save_user_data(user_data, file_name):
    """ Save user data to a binary file using pickling

    :param user_data: (dict) User data to be pickled
    :param file_name: (str) Name of the binary file
    :return: None
    """
    try:
        with open(file_name, "wb") as file:
            pickle.dump(user_data, file)
            print("User data pickled and saved successfully.")
    except Exception as e:
        print("Error pickling and saving user data:", e)


def load_user_data(file_name):
    """ Load user data from a pickled binary file

    :param file_name: (str) Name of the binary file
    :return: (dict) Loaded user data or None if file not found
    """
    try:
        with open(file_name, "rb") as file:
            loaded_data = pickle.load(file)
            return loaded_data
    except FileNotFoundError:
        print("User data file not found.")
        return None
    except Exception as e:
        print("Error loading user data:", e)
        return None


# Presentation ------------------------------------ #
user_data_file = "user_data.pkl"

# Saving user data using pickling
save_user_data(user_data, user_data_file)

# Loading user data from the pickled file
loaded_user_data = load_user_data(user_data_file)

if loaded_user_data:
    print("\nLoaded user data:", loaded_user_data)
    print("Username:", loaded_user_data['username'])
    print("Team:", loaded_user_data['team'])

# User input for continuing or getting more information
while True:
    try:
        choice = input("\nPress 1 to continue or type 'More' for more information: ")
        if choice == '1':
            break
        elif choice.lower() == 'more':
            print("\nThis section demonstrates the user input and error handling.")
            print("The highlighted code is responsible for handling user input.")
            print("In the loop, the program waits for the user to press 1 or type 'More'.")
            print("If the user enters anything else, an error is raised.")
        else:
            raise ValueError("Invalid choice. Please enter 1 or 'More'.")
    except ValueError as ve:
        print("Error:", ve)

print("\nContinuing with the script...")
