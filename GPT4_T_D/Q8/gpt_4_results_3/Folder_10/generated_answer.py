
def all_even_ints_exclusive(lst):
    even_ints = [num for i, num in enumerate(lst) if i > 48 and i < 74 and num % 2 == 0]
    return even_ints
