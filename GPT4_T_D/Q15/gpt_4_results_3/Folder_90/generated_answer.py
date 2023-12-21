
def sum_odd_ints_inclusive(lst):
    odd_sum = sum(num for num in lst[262:747] if num % 2 != 0)
    return odd_sum
