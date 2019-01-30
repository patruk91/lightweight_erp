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

table = data_manager.get_table_from_file(file_name="sales.csv")
title_list = ["Id", "Title", "Price", "Month", "Day", "Year"]


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

    elif check_if_data_is_in_range(i, integer_inputs, border_conditions):
        return True

    elif check_if_data_is_in_range(i, integer_inputs, border_conditions):
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
    sales_records = ["Enter title: ", "Enter price: ", "Enter month: ", "Enter day: ", "Enter year: "]
    border_conditions = ["", 10000000, 12, 31, 3000]
    new_record.append(common.generate_random(table))
    new_record.append(input(sales_records[0]))

    i = 1
    while i < len(sales_records):
        integer_inputs = input(sales_records[i])
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
    data_manager.write_table_to_file(file_name="sales.csv", table=update_table)
    show_table(update_table)
    return update_table


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
    options_of_update = ["title", "price", "month", "day", "year"]
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
            if options_of_update.index(user_input) + 1 == 1 or options_of_update.index(user_input) + 1 == 2:
                updated_record[0][options_of_update.index(user_input) + 1] = new_data
                ask_user += 1
            elif options_of_update.index(user_input) + 1 == 3 and new_data <= "12":
                updated_record[0][options_of_update.index(user_input) + 1] = new_data
                ask_user += 1
            elif options_of_update.index(user_input) + 1 == 4 and new_data <= "31":
                updated_record[0][options_of_update.index(user_input) + 1] = new_data
                ask_user += 1
            elif options_of_update.index(user_input) + 1 == 5 and len(new_data) == 4:
                updated_record[0][options_of_update.index(user_input) + 1] = new_data
                ask_user += 1
            else:
                print("Max amount of month is 12, of day is 31 and year must have four numbers!")
            for record in updated_record:
                if record[0] in table:
                    table = updated_record
            data_manager.write_table_to_file(file_name="sales.csv", table=table)
            ui.print_table(table, title_list)
        else:
            print("Something went wrong!")
            break
    return table
# special functions:
# ------------------

def get_lowest_price_item_id(table):
    """
    Question: What is the id of the item that was sold for the lowest price?
    if there are more than one item at the lowest price, return the last item by alphabetical order of the title

    Args:
        table (list): data table to work on

    Returns:
         string: id
    """
    price = min([int(price[2]) for price in table])
    title_with_min_price = [record[1] for record in table if int(record[2]) == price]
    sorted_title = common.handle_sort_names(title_with_min_price)
    result = [record[0] for record in table if record[1] == sorted_title[-1]]
    return result[0]


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