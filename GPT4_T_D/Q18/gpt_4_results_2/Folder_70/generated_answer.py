
def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[42:44]:
        if num % 15 == 0 or num % 87 == 0:
            total += num
    return total
