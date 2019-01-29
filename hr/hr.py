""" Human resources module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string)
    * birth_year (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


file_name = "persons.csv"
table = data_manager.get_table_from_file(file_name)
table_structure = ["Id", "Name", "Birth Year"]


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


# special functions:
# ------------------

def get_oldest_person(table):
    """
    Find the oldest persons
    :param table: list of lists with data form hr department
    :return: list with oldest persons name
    """

    oldest_year = min([record[2] for record in table])
    oldest_names = [name[1] for name in table if name[2] == oldest_year]
    return oldest_names


def get_persons_closest_to_average(table):
    """
    Find the person, which is closest to average age
    :param table: list of lists with data form hr department
    :return: list with persons, which is closet to average age
    """
    years = [int(year[2]) for year in table]
    years_avg = common.sum_values(years) / len(years)
    similar_years = min(years, key=lambda x: abs(x - years_avg))

    closest_person = [record[1] for record in table if int(record[2]) == similar_years]
    return closest_person
