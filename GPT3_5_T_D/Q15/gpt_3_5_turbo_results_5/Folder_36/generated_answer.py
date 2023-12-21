
def sum_odd_ints_inclusive(lst):
    odd_nums = [num for num in lst[246:751] if num % 2 == 1]
    return sum(odd_nums)
