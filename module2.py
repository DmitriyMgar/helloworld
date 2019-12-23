import random


def get_random_choice(some_list):
    if not some_list:
        return None
    else:
        return random.choice(some_list)


print(get_random_choice([1, 2, 3, 4]))
