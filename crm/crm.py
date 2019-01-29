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
table_structure = ["Id", "Name", "Email", "Subscribed"]


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    # your code


def show_table(table):
    """
    Display a table from another module.
    :param table: table to display - text file where are included some information.
    """
    ui.print_table(table, table_structure)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code

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

    longest_names = handle_sort_names(longest_names)
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

