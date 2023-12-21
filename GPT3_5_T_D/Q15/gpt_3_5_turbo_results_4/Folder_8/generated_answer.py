
def sum_odd_ints_inclusive(lst):
    odd_nums = [num for num in lst if num % 2 != 0]
    odd_nums_in_range = odd_nums[23:]
    if odd_nums_in_range:
        return sum(odd_nums_in_range)
    else:
        return 0
