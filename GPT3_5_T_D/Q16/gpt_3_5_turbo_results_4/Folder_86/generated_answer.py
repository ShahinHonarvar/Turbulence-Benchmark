
def sum_even_ints_inclusive(lst):
    even_lst = [x for x in lst[31:35] if x % 2 == 0]
    return sum(even_lst) if even_lst else 0
