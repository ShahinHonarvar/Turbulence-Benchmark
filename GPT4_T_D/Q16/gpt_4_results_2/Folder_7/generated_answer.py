
def sum_even_ints_inclusive(lst):
    evens = filter(lambda x: x % 2 == 0, lst[661:925])
    return sum(evens) if evens else 0
