
def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[55:81]:
        if num % 22 == 0 or num % 32 == 0:
            total += num
    return total
