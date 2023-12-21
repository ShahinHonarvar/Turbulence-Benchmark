
def sum_even_ints_inclusive(lst):
    sum_even = sum(n for n in lst[13:69] if n % 2 == 0)
    return sum_even if sum_even else 0
