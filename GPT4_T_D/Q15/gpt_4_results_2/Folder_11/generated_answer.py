
def sum_odd_ints_inclusive(lst):
    sublist = lst[37:52]
    odd_int_sum = sum(num for num in sublist if num % 2 != 0)
    return odd_int_sum
