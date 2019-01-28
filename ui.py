""" User Interface (UI) module """


def width_columns(table):
    """
    Find the longest width in table.
    :param table: table to display - text file where are included some information.
    :return: List with width of columns.
    """
    columns_width = []
    amount_of_columns = len(table[0])

    for index in range(amount_of_columns):
        column_width = 0
        for data in table:
            if column_width < len(data[index]):
                column_width = len(data[index])
        columns_width.append(column_width)

    return columns_width


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


def print_table(table, title_list):
    """
    Prints table with data.
    :param table: table to display - text file where are included some information.
    :param title_list: list containing table headers
    """
    columns_width = width_columns(table)
    amount_of_columns = len(columns_width)
    titles_width = (list(len(i) for i in title_list))
    total_width = [columns_width[i] if columns_width[i] > titles_width[i]
                   else titles_width[i] for i in range(amount_of_columns)]

    columns_keys = ["pos" + str(index) for index in range(amount_of_columns)]
    columns_dict = dict(zip(columns_keys, total_width))
    string = ''.join(
        ['| {:^{' + columns_keys[index] + '}} ' for index in range(amount_of_columns)]) + "|"
    sum_of_column_width = sum_values(
        total_width) + 1  # due to end in string "|"
    PADDINGS = 3

    print("-" * (sum_of_column_width + (amount_of_columns * PADDINGS)))
    for record in table:
        print(string.format(*record, **columns_dict))
        print("-" * (sum_of_column_width + (amount_of_columns * PADDINGS)))


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
