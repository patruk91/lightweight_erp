""" User Interface (UI) module """


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


def sum_values(numbers_list):
    """
    Sum values from list.
    :param numbers_list: List with integers.
    :return: sum(data_list)
    """
    sum_numbers = 0
    for number in numbers_list:
        sum_numbers += number
    return sum_numbers


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
    total_column_lenght = sum_values(width_columns) + 1  # due to end in var:string "|"
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
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []

    # your code

    return inputs


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
