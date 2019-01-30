""" Sales module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game sold
    * price (number): The actual sale price in USD
    * month (number): Month of the sale
    * day (number): Day of the sale
    * year (number): Year of the sale
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common

file_name="sales.csv"
table = data_manager.get_table_from_file(file_name)
title_list = ["Id", "Title", "Price", "Month", "Day", "Year"]

update_options = ["title", "price", "month", "day", "year"]
border_conditions = ["", 10000000, 12, 31, 3000]

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
        id_ = input("Enter id of record to delete: ")
        remove(table, id_)
    elif option == "4":
        ui.print_table(table, title_list)
        id_ = input("Enter id of record who you want edit: ")
        update(table, id_)
    elif option == "5":
        get_lowest_price_item_id(table)
    elif option == "6":
        get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to)
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def show_table(table):
    """
    Display a table from another module.
    :param table: table to display - text file where are included some information.
    """
    ui.print_table(table, title_list)


def check_if_input_is_number(integer_inputs):
    if integer_inputs.isdigit() and int(integer_inputs) > 0:
        return True
    return False


def evaluate_user_input(i, integer_inputs, border_conditions):
    if check_if_data_is_in_range(i, integer_inputs, border_conditions):
        return True
    return False


def check_if_data_is_in_range(i, integer_inputs, border_conditions):
    if i != 2 and i != 3 and int(integer_inputs) <= border_conditions[i]:
        return True
    elif i == 2:
        if int(integer_inputs) <= border_conditions[i]:
            return True
    elif i == 3:
        if int(integer_inputs) <= border_conditions[i]:
            return True
    return False


def add(table):
    """
    Asks user for input and adds it into the table.
    :param table: text file where are included some information.
    :return: list with a new record
    """
    new_record = []

    new_record.append(common.generate_random(table))
    new_record.append(input(update_options[0]))

    i = 1
    while i < len(update_options):
        integer_inputs = input("Enter" + update_options[i])
        if check_if_input_is_number(integer_inputs):
            if evaluate_user_input(i, integer_inputs, border_conditions):
                new_record.append(integer_inputs)
                i += 1
        else:
            print("error!")

    updated_table = table + [new_record]
    data_manager.write_table_to_file(file_name="sales.csv", table=updated_table)
    show_table(updated_table)

    return updated_table


def remove(table, id_):
    """
    Remove a record with a given id from the table.
    :param table: text file where are included some information.
    :param id_: id/key record to be removed
    :return: list without specified record.
    """
    update_table = [records for records in table if id_ not in records]
    data_manager.write_table_to_file(file_name, table=update_table)
    show_table(update_table)
    return update_table


def handle_chosen_options():
    pass


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.
    :param table: text file where are included some information.
    :param id_: id of a record to update
    :return: list of list with updated record
    """
    searched_record = [record for record in table if id_ in record]
    ui.print_table(searched_record, title_list)
    searched_record = searched_record[0]  # unpack from list of lists
    id_place = 1
    # due to id in on the 0 position in list

    i = 0
    while i < 1:
        user_input = input("What do you want change?").lower()
        if user_input in update_options:
            chosen_option = update_options.index(user_input) + id_place
            new_data = input("Actual " + user_input + ": "
                             + searched_record[chosen_option]
                             + "\nEnter new: ")

            if chosen_option == 1:
                searched_record[chosen_option] = new_data
                i += 1
            elif check_if_input_is_number(new_data) and evaluate_user_input(
                    chosen_option - + id_place, new_data, border_conditions):
                searched_record[chosen_option] = new_data
                i += 1
            else:
                print("some kind of error, to wide range for day month year etc")
        else:
            print("Provide correct value")
    data_manager.write_table_to_file(file_name, table=table)
    ui.print_table([searched_record], title_list)
    return table

print(update(table, id_="kH35Jr#&"))

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """

    # your code


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Question: Which items are sold between two given dates? (from_date < sale_date < to_date)

    Args:
        table (list): data table to work on
        month_from (int)
        day_from (int)
        year_from (int)
        month_to (int)
        day_to (int)
        year_to (int)

    Returns:
        list: list of lists (the filtered table)
    """

    # your code
start_module()