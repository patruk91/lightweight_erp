# User interface module
import ui
# data manager module
import data_manager
# common module
import common

file_name = "items.csv"
table = data_manager.get_table_from_file(file_name)
title_list = ["Id", "Month", "Day", "Year", "Type", "Amount ($)"]
update_options = ["month", "day", "year", "type", "amount"]
border_conditions = [12, 31, 3000, "", 3000000]


def start_module():
    """
    Menu of this file.
    """
    answer = common.accounting_sub_menu()
    if answer == "1":
        show_table(table)
    elif answer == "2":
        add(table)
    elif answer == "3":
        id_ = input("Enter id of record to delete: ")
        remove(table, id_)
    elif answer == "4":
        show_table(table)
        id_ = input("Enter id of record to delete: ")
        update(table, id_)
    elif answer == "5":
        which_year_max(table)
    elif answer == "6":
        avg_amount(table, year)
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
        if i == 3:
            new_record.append(handle_inputs)
            i += 1
        else:
            if common.check_if_input_is_number(handle_inputs):
                if common.check_if_data_is_in_range(i, handle_inputs, border_conditions):
                    new_record.append(handle_inputs)
                    i += 1
            else:
                ui.print_error_message("Something went wrong!")
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

            if chosen_option == 4:
                searched_record[chosen_option] = new_data
                i += 1
            elif common.check_if_input_is_number(new_data) and common.check_if_data_is_in_range(
                    chosen_option - + id_place, new_data, border_conditions):
                searched_record[chosen_option] = new_data
                i += 1
            else:
                ui.print_error_message("some kind of error, to wide range for day month year etc")
        else:
            ui.print_error_message("Provide correct value")
    data_manager.write_table_to_file(file_name, table=table)
    ui.print_table([searched_record], title_list)
    return table


def which_year_max(table):
    """
    Find the year where was highest income.
    :param table: list of lists with data form account department
    :return: max year numer
    """
    transactions = [(amount[4], int(amount[5])) for amount in table]
    max_amount = max([int(amount[5]) for amount in table])
    year_index = [index for index in range(len(transactions))
                  if transactions[index][1] == max_amount and
                  transactions[index][0] == "in"]
    if len(year_index) > 1:
        years_max = [int(table[year_index[index]][3]) for index in range(len(year_index))]
        return years_max

    year_max = table[year_index[0]][3]
    show_table([table[year_index[0]]])
    return year_max


def avg_amount(table, year):
    """
    Calculate average (per item) profit in a given year.
    :param table: list of lists with data form account department
    :param year: find the biggest profit by year
    :return: profit = (income - outflow)/(items count)
    """
    year_by_income = [(record[4], int(record[5])) for record in table if int(record[3]) == year]
    income = [wages[1] for wages in year_by_income if wages[0] == "in"]
    outflow = [wages[1] for wages in year_by_income if wages[0] == "out"]
    profit = (common.sum_values(income) - common.sum_values(outflow)) / len(year_by_income)

    return profit
