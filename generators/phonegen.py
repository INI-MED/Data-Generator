
from random import randint
from random import choice

patterns = ["8999", "8950", "8920", "8910", "8951", "8952", "8921", "8990"]


def random_with_N_digits(n, how_many):
    phones = []
    while how_many > 0:
        range_start = 10**(n-1)
        range_end = (10**n)-1
        phone_range = choice(patterns) + str(randint(range_start, range_end))
        if phone_range not in phones:
            phones.append(phone_range)
            how_many -= 1
        return phone_range
