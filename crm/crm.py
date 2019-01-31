""" Customer Relationship Management (CRM) module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * email (string)
    * subscribed (int): Is she/he subscribed to the newsletter? 1/0 = yes/no
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


file_name = "customers.csv"
table = data_manager.get_table_from_file(file_name)
title_list = ["Id", "Name", "Email", "Subscribed"]

update_options = ["name", "email", "subscribed"]
border_conditions = ["", "", "", ""]


def start_module():
    """
    Menu of this file.
    """
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
        get_longest_name_id(table)
    elif option == "6":
        get_subscribed_emails(table)
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

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code

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

    # your code

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


# the question: Which customers has subscribed to the newsletter?
# return type: list of strings (where string is like email+separator+name, separator=";")
def get_subscribed_emails(table):
    """
    Find customers has subscribed the newsletter.
    :param table: list of lists with data form crm department
    :return: list with subscribed customers
    """
    subscribed_emails = [record[2] + ";" + record[1] for record in table if int(record[3]) == 1]
    return subscribed_emails

start_module()