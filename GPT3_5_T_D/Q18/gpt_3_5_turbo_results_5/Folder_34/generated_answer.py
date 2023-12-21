
def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[60:201]:
        if num % 9 == 0 or num % 11 == 0:
            total += num
    return total
