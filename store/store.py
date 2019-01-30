""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common
table = data_manager.get_table_from_file(file_name="games.csv")
title_list = ["Id", "Title", "Manufacturer", "Price", "In stock"]

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
        show_table(table)
        id_ = input("Enter id of record to delete: ")
        remove(table, id_)
    elif option == "4":
        show_table(table)
        id_ = input("Enter id of record who you want edit: ")
        update(table, id_)
    elif option == "5":
        get_counts_by_manufacturers(table)
    elif option == "6":
        get_average_by_manufacturer(table)
    elif option == "0":
        sys.exit(0)
    else:
        raise KeyError("There is no such option.")


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    # your code


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
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code

    return table


def get_counts_by_manufacturers(table):
    """
    Display counts of games for each manufacturer
    :param table: list of all items in database
    :return: dictionary ith results
    """
    list_of_manufacturer = []
    kinds_and_manufacturer = [(record[1], record[2]) for record in table]
    for records in table:
        if records[2] not in list_of_manufacturer:
            list_of_manufacturer.append(records[2])
    list_of_kinds_of_games = [[games[0] for games in
                               kinds_and_manufacturer if company == games[1]]
                              for company in list_of_manufacturer]
    count_of_games = [len(games) for games in list_of_kinds_of_games]
    dict_of_counts_by_manufacturer = dict(zip(list_of_manufacturer, count_of_games))
    return dict_of_counts_by_manufacturer


def get_average_by_manufacturer(table, manufacturer="Ensemble Studios"):
    """
    Display calculated average of games amount in stock for given manufacturer
    :param table: list of all items in database
    :param manufacturer: Name of manufacturer
    :return: Average of games amount in stock
    """
    ui.print_table(table, title_list)
    manufacturer_and_stock = [(record[2], record[4]) for record in table if record[2] == manufacturer]
    list_of_amount_in_stock = [int(games[1]) for games in
                               manufacturer_and_stock if games[0] == manufacturer]
    avg_count = [common.sum_values(list_of_amount_in_stock) / len(list_of_amount_in_stock)]
    return avg_count[0]
