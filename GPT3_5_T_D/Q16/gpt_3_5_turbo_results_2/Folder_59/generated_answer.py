
def sum_even_ints_inclusive(lst):
    even_nums = [n for n in lst[:10] if n % 2 == 0]
    return sum(even_nums)
