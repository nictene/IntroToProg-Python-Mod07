#.....................................#
# Title: Home Inventory tracker
# Desc: This scripts creates a csv file and inputs user data into it like a spreadsheet.
#       the sum, difference, product and quotient
# Change Log: (ntenev on 8-11-2023)
# NTenev,  08-02-2023, modified to include csv
#.....................................#
import csv

# Create an empty list to store household item data as rows
household_items = []

# Infinite loop to keep asking for household items and their values
while True:
    # Ask the user for the name of the household item
    item_name = input("Enter the name of the household item (or 'exit' to quit): ")

    # Check if the user wants to exit the loop
    if item_name.lower() == 'exit':
        break  # Exit the loop

    # Ask the user for the estimated value of the household item
    item_value = input("Enter the estimated value of the household item: ")

    # Create a row of data with the item name and value, and append it to the list
    item_data = [item_name, item_value]
    household_items.append(item_data)

# Save the collected household item data to a CSV file
csv_filename = "household_items.csv"
with open(csv_filename, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["Item Name", "Estimated Value"])  # Write header
    csv_writer.writerows(household_items)  # Write data rows

print("Household item data saved to", csv_filename)

# End of the script
print("Data collection completed.")
