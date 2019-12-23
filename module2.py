import random


def get_random_choice(some_list):
    if not some_list:
        return None
    else:
        my_choice = random.choice(some_list)
        print("Я выбрал {}".format(my_choice))
        return my_choice


print(get_random_choice([1, 2, 3, 4]))
