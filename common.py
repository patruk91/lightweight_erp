""" Common module
implement commonly used functions here
"""

import random


def generate_random(table):
    """
    Generates random and unique string.
    :param table: list of lists with data from account department
    :return: Random unique id/key
    """
    unique_values = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                     "1234567890", "\`~!@#$%^&*()_-+={[}}|:,'<>?/"]
    while True:
        string_generator = [random.choice(char) for char in unique_values for _ in range(2)]
        random.shuffle(string_generator)
        generated = "".join(string_generator)
        id_list = [id_key[0] for id_key in table]
        if generated not in id_list:
            return generated


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


def handle_sort_names(longest_names):
    """
    Sort the string data in ascending order.
    :param longest_names: Name of people to sort.
    :return: list with sorted names
    """
    x = 0
    while x < len(longest_names):
        for index in range(len(longest_names) - 1):
            if longest_names[index] > longest_names[index + 1]:
                temp = longest_names[index + 1]
                longest_names[index + 1] = longest_names[index]
                longest_names[index] = temp
        x += 1
    return longest_names


def check_if_input_is_number(handle_inputs):
    """
    Check if input parameter is number.
    :param handle_inputs: parameters provided from user.
    :return: boolean
    """
    if handle_inputs.isdigit() and int(handle_inputs) > 0:
        return True
    return False

def check_if_data_is_in_range(i, handle_inputs, border_conditions):
    """
    Check if data provided from user is in definded border conditions.
    :param i: iterator from loop
    :param handle_inputs: parameters provided from user.
    :param border_conditions: list with maximum acceptable
    :return: boolean
    """
    if i != 2 and i != 3 and int(handle_inputs) <= border_conditions[i]:
        return True
    elif i == 2:
        if int(handle_inputs) <= border_conditions[i]:
            return True
    elif i == 3:
        if int(handle_inputs) <= border_conditions[i]:
            return True
    return False


def store_sub_menu():
    print("""
        (1)Show table
        (2)Add
        (3)Remove
        (4)Update
        (5)Get counts by manufacturers
        (6)Get average by manufacturers""")
    answer = input("Choose number: ")
    return answer


def hr_sub_menu():
    print("""
        (1)Show table
        (2)Add
        (3)Remove
        (4)Update
        (5)Get oldest person
        (6)Get persons closest to average""")
    answer = input("Choose number: ")
    return answer


def inventory_sub_menu():
    print("""
            (1)Show table
            (2)Add
            (3)Remove
            (4)Update
            (5)Get available items
            (6)Get average durability by manufacturers""")
    answer = input("Choose number: ")
    return answer


def accounting_sub_menu():
    print("""
            (1)Show table
            (2)Add
            (3)Remove
            (4)Update
            (5)Find the year where was highest income
            (6)Calculate average (per item) profit in a given year""")
    answer = input("Choose number: ")
    return answer


def sales_sub_menu():
    print("""
        (1)Show table
        (2)Add
        (3)Remove
        (4)Update
        (5)Get lowest price item id
        (6)Get items sold between""")
    answer = input("Choose number: ")
    return answer


def crm_sub_menu():
    print("""
        (1)Show table
        (2)Add
        (3)Remove
        (4)Update
        (5)Find id of the customer with the longest name.
        (6)Find customers has subscribed the newsletter.""")
    answer = input("Choose number: ")
    return answer
