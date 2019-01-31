# User interface module
import ui
# data manager module
import data_manager
# common module
import common

file_name = "./sales/sales.csv"
table = data_manager.get_table_from_file(file_name)
title_list = ["Id", "Title", "Price", "Month", "Day", "Year"]

update_options = ["title", "price", "month", "day", "year"]
border_conditions = ["", 10000000, 12, 31, 3000]


def start_module():

    inputs = input("Please enter a number: ")
    option = inputs[0]
    if option == "1":
        show_table(table)
    elif option == "2":
        add(table)
    elif option == "3":
        show_table(table)
        id_ = input("Enter id of record to delete: ")
        remove(table, id_)
    elif option == "4":
        ui.print_table(table, title_list)
        id_ = input("Enter id of record who you want edit: ")
        update(table, id_)
    elif option == "5":
        get_lowest_price_item_id(table)
    elif option == "6":
        get_items_sold_between(table, month_from=2, day_from=12, year_from=2016, month_to=7, day_to=6, year_to=2016)
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


def add(table):
    """
    Asks user for input and adds it into the table.
    :param table: text file where are included some information.
    :return: list with a new record
    """
    new_record = []
    new_record.append(common.generate_random(table))
    new_record.append(input("Enter " + update_options[0] + ": "))
    i = 1
    while i < len(update_options):
        handle_inputs = input("Enter " + update_options[i] + ": ")
        if common.check_if_input_is_number(handle_inputs):
            if common.check_if_data_is_in_range(i, handle_inputs, border_conditions):
                new_record.append(handle_inputs)
                i += 1
        else:
            print("error!")

    updated_table = table + [new_record]
    data_manager.write_table_to_file(file_name, table=updated_table)
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
            elif common.check_if_input_is_number(new_data) and common.check_if_data_is_in_range(
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


def get_lowest_price_item_id(table):
    """
    Display lowest price in database by given id
    :param table: list of all items in database
    :return: title of item with lowest price
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
