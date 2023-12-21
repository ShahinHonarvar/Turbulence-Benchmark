
def all_even_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i > 0 and i < 8 and num % 2 == 0]
