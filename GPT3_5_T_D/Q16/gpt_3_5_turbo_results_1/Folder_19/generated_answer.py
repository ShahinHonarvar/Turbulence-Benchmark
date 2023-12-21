
def sum_even_ints_inclusive(lst):
    evens = [x for x in lst[3:6] if x % 2 == 0]
    return sum(evens)
