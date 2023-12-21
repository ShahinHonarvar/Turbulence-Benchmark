
def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[34:82]:
        if num % 27 == 0 or num % 57 == 0:
            total += num
    return total
