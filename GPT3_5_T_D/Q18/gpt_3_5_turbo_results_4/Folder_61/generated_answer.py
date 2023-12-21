
def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[:7]:
        if num % -5 == 0 or num % -6 == 0:
            total += num
    return total
