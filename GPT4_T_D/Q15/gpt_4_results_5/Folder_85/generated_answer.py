
def sum_odd_ints_inclusive(lst):
    odd_nums = [num for num in lst[6:9] if num % 2 != 0]
    if not odd_nums:
        return 0
    else:
        return sum(odd_nums)
