
def sum_odd_ints_inclusive(lst):
    odd_nums = [num for num in lst[28:41] if num % 2 != 0]
    return sum(odd_nums) if len(odd_nums) > 0 else 0
