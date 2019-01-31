import ui
# data manager module
import data_manager
# common module
import common

file_name = "inventory.csv"
table = data_manager.get_table_from_file(file_name)
title_list = ["Id", "Title", "Price", "Month", "Day"]

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
    new_list = []
    for records in table:
        if id_ not in records:
            new_list.append(records)
        data_manager.write_table_to_file(file_name="inventory.csv", table=new_list)
    show_table(new_list)
    return new_list


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.
    :param table: list of all items in database
    :param id_: input where user enter id
    :return: updated table
    """
    updated_record = []
    options_of_update = ["name", "manufacturer", "purchase", "years"]
    for record in table:
        if id_ in record:
            updated_record.append(record)
    show_table(updated_record)
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
        show_table(table)
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