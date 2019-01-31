# User interface module
import ui
# data manager module
import data_manager
# common module
import common

file_name = "./sales/sales.csv"
table = data_manager.get_table_from_file(file_name)
title_list = ["Id", "Title", "Price", "Month", "Day", "Year"]

update_options = ["title", "price", "month", "day", "year"]
border_conditions = ["", 10000000, 12, 31, 3000]


def start_module():

    answer = common.sales_sub_menu()
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
        get_lowest_price_item_id(table)
    elif answer == "6":
        from_data = get_data('Start date')
        to_data = get_data('End data')
        get_items_sold_between(table, month_from=from_data[1], day_from=from_data[2],\
                               year_from=from_data[0], month_to=to_data[1], day_to=to_data[2], year_to=to_data[0])
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


def get_lowest_price_item_id(table):
    """
    Display lowest price in database by given id
    :param table: list of all items in database
    :return: title of item with lowest price
    """
    price = min([int(price[2]) for price in table])
    title_with_min_price = [record[1] for record in table if int(record[2]) == price]
    sorted_title = common.handle_sort_names(title_with_min_price)
    result = [record[0] for record in table if record[1] == sorted_title[-1]]
    return result[0]


def get_items_sold_between(table, month_from, day_from, year_from, month_to, day_to, year_to):
    """
    Display items are sold between two given dates
    :param table: list of all items in database
    :param month_from: month given by user to define start range of search
    :param day_from: day given by user to define start range of search
    :param year_from: year given by user to define start range of search
    :param month_to: month given by user to define end range of search
    :param day_to: day given by user to define end range of search
    :param year_to: year given by user to define end range of search
    :return: list of records who fulfills given range of date
    """
    YEAR_I = 5
    MONTH_I = 3
    DAY_I = 4
    from_date = join_to_digit(year_from, month_from, day_from)
    to_date = join_to_digit(year_to, month_to, day_to)
    result = []
    for entry in table:
        entry_data = join_to_digit(entry[YEAR_I], entry[MONTH_I], entry[DAY_I])
        if from_date < entry_data < to_date:
            result.append(entry)
    if len(result) > 0:
        show_table(result)
    else:
        ui.print_error_message("No records in this range!")

    return result


def join_to_digit(year, month, day):
    """
    Tomorrow will be docstring....
    :param year:
    :param month:
    :param day:
    :return:
    """
    date = []
    date.append(str(year))

    if len(str(month)) < 2:
        month = '0' + str(month)
        date.append(month)
    else:
        date.append(str(month))

    if len(str(day)) < 2:
        day = '0' + str(day)
        date.append(day)
    else:
        date.append(str(day))

    return int(''.join(date))


def validate_digit(input, start_range, end_range, error_type):
    digit = int(input)
    if digit < start_range or digit > end_range:
        raise error_type


def get_data(title):
    ui.print_error_message(title)
    data = []
    for i in range(3):
        while True:
            try:
                if i == 0:
                    year = ui.get_inputs([''], 'Enter year: ')[0]
                    validate_digit(year, 0, 2019, ConnectionError)
                    data.append(year)
                    break
                elif i == 1:
                    month = ui.get_inputs([''], 'Enter month: ')[0]
                    validate_digit(month, 1, 12, PermissionError)
                    data.append(month)
                    break
                elif i == 2:
                    day = ui.get_inputs([''], 'Enter day: ')[0]
                    validate_digit(day, 1, 31, ProcessLookupError)
                    data.append(day)
                    break
            except (ValueError, TypeError):
                ui.print_error_message('It need to be a digit.')
            except ConnectionError:
                ui.print_error_message('Year must be between 0 and 2019.')
            except PermissionError:
                ui.print_error_message('Month must be between 1 and 12.')
            except ProcessLookupError:
                ui.print_error_message('Day must be between 1 and 31.')

    return data

