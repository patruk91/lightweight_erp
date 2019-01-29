""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

table = data_manager.get_table_from_file(file_name="inventory.csv")
title_list = ["Id", "Name of item", "Manufacturer", "Year of purchase", "Years it can be used"]
def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    inputs = input(["Please enter a number: "])
    option = inputs[0]
    if option == "1":
        show_table(table)
    elif option == "2":
        add(table)
    elif option == "3":
        ui.print_table(table, title_list)
        id_ = input("Enter id of record to delete: ")
        remove(table, id_)
    elif option == "4":
        ui.print_table(table, title_list)
        id_ = input("Enter id of record who you want edit: ")
        update(table, id_)
    elif option == "5":
        sales.start_module()
    elif option == "6":
        crm.start_module()
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def show_table(table):
    """
    Display records from file in table
    """
    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    new_record = []
    inventory_records = ["Enter name of item: ", "Enter manufacturer: ", "Enter year of purchase: ",
                         "Enter years how can be used: "]
    new_record.append(common.generate_random(table))
    i = 0
    while i < 2:
        user_input = input(inventory_records[i])
        new_record.append(user_input)
        i += 1
    i = 2
    while i < len(inventory_records):
        integer_inputs = input(inventory_records[i])
        if integer_inputs.isdigit():
            new_record.append(integer_inputs)
            i += 1
        else:
            ui.print_error_message("Enter numbers!")
    updated_table = table + [new_record]
    data_manager.write_table_to_file(file_name="inventory.csv", table=updated_table)
    ui.print_table(updated_table, title_list)
    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    new_list = []
    for records in table:
        if id_ not in records:
            new_list.append(records)
        data_manager.write_table_to_file(file_name="inventory.csv", table=new_list)
    ui.print_table(new_list, title_list)
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    updated_record = []
    options_of_update = ["name", "manufacturer", "purchase", "years"]
    for record in table:
        if id_ in record:
            updated_record.append(record)
    ui.print_table(updated_record, title_list)
    user_input = input("What do you want change ?").lower()
    ask_user = 0
    while ask_user < 1:
        new_data = input("Actual " + user_input + ": " +
                         updated_record[0][options_of_update.index(user_input) + 1] + "\nEnter new: ")
        if user_input in options_of_update:
            updated_record[0][options_of_update.index(user_input) + 1] = new_data
            ask_user += 1
        else:
            ui.print_error_message("No option i database to change!")
        for record in updated_record:
            if record[0] in table:
                table = updated_record
        data_manager.write_table_to_file(file_name="inventory.csv", table=table)
        ui.print_table(table, title_list)
    return table
# special functions:
# ------------------

def get_available_items(table):
    """
    Question: Which items have not exceeded their durability yet?

    Args:
        table (list): data table to work on

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    # your code


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    # your code
