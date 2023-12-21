
def sum_odd_ints_inclusive(lst):
    odd_nums = [num for num in lst[75:86] if num % 2 != 0]
    return sum(odd_nums)
