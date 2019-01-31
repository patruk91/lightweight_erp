# User interface module
import ui
# data manager module
import data_manager
# common module
import common

file_name = "./crm/customers.csv"
table = data_manager.get_table_from_file(file_name)
title_list = ["Id", "Name", "Email", "Subscribed"]
update_options = ["name", "email", "subscribed"]
border_conditions = ["", "", 1]


def start_module():
    """
    Menu of this file.
    """
    answer = common.crm_sub_menu()
    if answer == "1":
        show_table(table)
    elif answer == "2":
        add(table)
    elif answer == "3":
        show_table(table)
        id_ = input("Enter id of record to delete: ")
        remove(table, id_)
    elif answer == "4":
        ui.print_table(table, title_list)
        id_ = input("Enter id of record who you want edit: ")
        update(table, id_)
    elif answer == "5":
        get_longest_name_id(table)
    elif answer == "6":
        get_subscribed_emails(table)
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
    i = 0
    while i < len(update_options):
        handle_inputs = input("Enter " + update_options[i] + ": ")
        new_record.append(handle_inputs)
        i += 1
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
            searched_record[chosen_option] = new_data
            i += 1
        else:
            print("Provide correct value")
    data_manager.write_table_to_file(file_name, table=table)
    ui.print_table([searched_record], title_list)
    return table


def get_longest_name_id(table):
    """
    Find id of the customer with the longest name.
    :param table: list of lists with data form crm department
    :return: Id of the longest name (if there are more than one, return
                the last by alphabetical order of the names)
    """
    names = [(len(record[1]), record[1]) for record in table]
    max_len_name = max([value[0]for value in names])
    longest_names = [name[1] for name in names if name[0] == max_len_name]

    longest_names = common.handle_sort_names(longest_names)
    get_index_name = [index for index, name in enumerate(names) if name[1] == longest_names[-1]][0]

    return table[get_index_name][0]


def get_subscribed_emails(table):
    """
    Find customers has subscribed the newsletter.
    :param table: list of lists with data form crm department
    :return: list with subscribed customers
    """
    subscribed_emails = [record[2] + ";" + record[1] for record in table if int(record[3]) == 1]
    return subscribed_emails
