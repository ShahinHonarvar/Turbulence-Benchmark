
def sum_even_ints_inclusive(lst):
    even_nums = [i for i in lst[70:85] if i % 2 == 0]
    return sum(even_nums) if even_nums else 0
