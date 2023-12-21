
def sum_odd_ints_inclusive(lst):
    odd_sum = sum(num for index, num in enumerate(lst[19:93]) if num % 2 != 0)
    return odd_sum
