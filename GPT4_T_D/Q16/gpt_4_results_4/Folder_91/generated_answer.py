
def sum_even_ints_inclusive(lst):
    return sum(num for num in lst[:6] if num % 2 == 0)
