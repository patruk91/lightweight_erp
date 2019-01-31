import ui
# data manager module
import data_manager
# common module
import common

file_name = "inventory.csv"
table = data_manager.get_table_from_file(file_name)
title_list = ["Id", "Title", "Price", "Month", "Day"]
actual_year = 2019
update_options = ["title", "price", "month", "day"]
border_conditions = ["", 10000000, 12, 31]


def start_module():
    """
    Menu of this file.
    """
    inputs = input(["Please enter a number: "])
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
        show_table(table)
        id_ = input("Enter id of record who you want edit: ")
        update(table, id_)
    elif option == "5":
        get_available_items(table)
    elif option == "6":
        get_average_durability_by_manufacturers(table)
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
    :param table: list of all items in database
    :return: updated table
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
    :param table: list of all items in database
    :param id_: input where user enter id
    :return: list with a new record
    """
    update_table = [records for records in table if id_ not in records]
    data_manager.write_table_to_file(file_name, table=update_table)
    show_table(update_table)
    return update_table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.
    :param table: list of all items in database
    :param id_: input where user enter id
    :return: updated table
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


def get_available_items(table):
    """
    Display items with actual durability
    :param table: list of all items in database
    :return: list of items with actual durability
    """
    actual_durability = [record for record in table if
                         int(record[3]) + int(record[4]) >= actual_year]
    show_table(actual_durability)
    return actual_durability


def get_average_durability_by_manufacturers(table):
    """
    Display average durability by manufacturers
    :param table: list of all items in database
    :return: dictionary with average of durability
    """
    list_of_manufacturer = []
    companies_durability = [(record[2], record[4]) for record in table]

    for records in table:
        if records[2] not in list_of_manufacturer:
            list_of_manufacturer.append(records[2])

    list_of_durability = [[int(company_dur[1]) for company_dur in
                           companies_durability if company == company_dur[0]]
                          for company in list_of_manufacturer]

    average_durability = [str(common.sum_values(num_list) / len(num_list))
                          for num_list in list_of_durability]

    convert_avg_dur = [int(float(num)) if ".0" in num else float(num)
                       for num in average_durability]

    dict_avg_dur = dict(zip(list_of_manufacturer, convert_avg_dur))
    return dict_avg_dur

start_module()