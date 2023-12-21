
def sum_even_ints_inclusive(lst):
    sum_even = sum(ele for ele in lst[8:10] if ele % 2 == 0)
    return sum_even if sum_even else 0
