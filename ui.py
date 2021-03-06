""" User Interface (UI) module """
import common


def get_width_columns(table, title_list):
    """
    Find the longest width in table.
    :param table: table to display - text file where are included some information.
    :return: List with width of columns.
    """
    number_of_columns = len(table[0])
    file_columns_width = [max([len(data[index]) for data in table])
                          for index in range(number_of_columns)]

    titles_width = (list(len(title) for title in title_list))
    width_columns = [file_columns_width[index] if file_columns_width[index] >
                     titles_width[index] else titles_width[index]
                     for index in range(number_of_columns)]

    return width_columns



def get_position_value_dictionary(table, title_list):
    """
    Create a dictionary with position and column width. Is need to **kwargs
    in print table function.
    :return: Dictionary with position:column width
    """
    width_columns = get_width_columns(table, title_list)
    number_of_columns = len(width_columns)
    string_positions = ["pos" + str(index) for index in range(number_of_columns)]
    position_value = dict(zip(string_positions, width_columns))

    return position_value


def get_total_sum_of_width_columns(table, title_list):
    """
    Calcualte total sum of width in each column.
    :param table: table: table to display - text file where are included some information.
    :param title_list: title_list: list containing table headers
    :return: Sum of width
    """
    width_columns = get_width_columns(table, title_list)
    total_column_lenght = common.sum_values(width_columns) + 1  # due to end in var:string "|"
    number_of_columns = len(width_columns)
    PADDINGS = 3

    total_width_sum = total_column_lenght + (number_of_columns * PADDINGS)
    return total_width_sum


def print_table(table, title_list):
    """
    Prints table with data.
    :param table: table to display - text file where are included some information.
    :param title_list: list containing table headers
    """
    dict_pos_value = get_position_value_dictionary(table, title_list)
    total_width_sum = get_total_sum_of_width_columns(table, title_list)
    string = ''.join(['| {:^{' + pos + '}} ' for pos in dict_pos_value.keys()]) + "|"

    print("-" * total_width_sum)
    print(string.format(*title_list, **dict_pos_value))

    print("-" * total_width_sum)
    for record in table:
        print(string.format(*record, **dict_pos_value))
        print("-" * total_width_sum)


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code


def print_menu(title, list_options, exit_message):
    """
    Displays a menu.
    :param title: menu title
    :param list_options: list of strings - options that will be shown in menu
    :param exit_message: option for back to main menu
    """
    print("{}:" .format(title))
    i = 1
    for option in list_options:
        print("({}) {}" .format(i, option))
        i += 1
    print("(0) {}" .format(exit_message))


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    :param list_labels: labels of inputs
    :param title: title of the "input section"
    :return: list of data given by the user
    """
    print("{}:" .format(title))
    inputs = []
    for label in list_labels:
        answers = input("{}: " .format(label))
        inputs.append(answers)

    return inputs


def print_error_message(message):
    """
    Displays an error message
    :param message: error message to be displayed
    """
    print("{}" .format(message))
