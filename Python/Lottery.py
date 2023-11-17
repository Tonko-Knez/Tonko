# Lottery simulation

import random

lucky_combination = []

def lottery():
        i = 0
        list_of_numbers = list(range(1,40))

        while i < 7:
                withdrawn_number = random.choice(list_of_numbers)
                lucky_combination.append(withdrawn_number)
                list_of_numbers.remove(withdrawn_number)
                i += 1
                print(withdrawn_number)
                print(list_of_numbers)
                print(lucky_combination)
        else:
                return lucky_combination

lottery()

print("The lucky combination is", lucky_combination)
