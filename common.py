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
