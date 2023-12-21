
def sum_even_ints_inclusive(lst):
    even_nums = [num for num in lst[19:93] if num % 2 == 0]
    return sum(even_nums)
