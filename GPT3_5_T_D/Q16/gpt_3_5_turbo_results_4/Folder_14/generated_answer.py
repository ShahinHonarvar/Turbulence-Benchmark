
def sum_even_ints_inclusive(lst):
    even_nums = [x for x in lst[5:8] if x % 2 == 0]
    return sum(even_nums) if even_nums else 0
