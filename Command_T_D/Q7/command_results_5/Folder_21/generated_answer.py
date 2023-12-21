
def all_even_ints_inclusive(ints):
    evens = [x for x in range(639, 975 + 1) if x % 2 == 0]
    return evens if evens in ints else []
