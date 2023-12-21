
def sum_even_ints_inclusive(lst):
    evens = [x for x in lst[25:60] if x % 2 == 0]
    return sum(evens) if evens else 0
