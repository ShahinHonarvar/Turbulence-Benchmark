
def sum_odd_ints_inclusive(lst):
    lst = lst[20:201]
    odd_sum = sum(num for num in lst if num % 2 != 0)
    return odd_sum
