
def sum_even_ints_inclusive(lst):
    evens = [n for n in lst[28:41] if n % 2 == 0]
    return sum(evens) if evens else 0
