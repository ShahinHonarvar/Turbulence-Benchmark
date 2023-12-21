
def sum_even_ints_inclusive(lst):
    range_lst = lst[29:80]
    even_lst = [num for num in range_lst if num % 2 == 0]
    return sum(even_lst) if even_lst else 0
